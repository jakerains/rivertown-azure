import { AzureKeyCredential } from '@azure/openai';
import { OpenAIClient } from '@azure/openai';
import { SearchClient, SearchDocument as BaseSearchDocument } from '@azure/search-documents';
import { StreamingTextResponse, Message } from 'ai';
import { join } from 'path';
import { readFileSync } from 'fs';

// Initialize Azure clients
const openAIClient = new OpenAIClient(
  process.env.AZURE_OPENAI_ENDPOINT!,
  new AzureKeyCredential(process.env.AZURE_OPENAI_API_KEY!)
);

const searchClient = new SearchClient(
  process.env.AISEARCH_ENDPOINT!,
  process.env.AISEARCH_INDEX_NAME!,
  new AzureKeyCredential(process.env.AISEARCH_KEY!)
);

// Load prompt templates
const ASSET_PATH = join(process.cwd(), 'assets');
const intentMappingPrompt = readFileSync(join(ASSET_PATH, 'intent_mapping.prompty'), 'utf-8');
const groundedChatPrompt = readFileSync(join(ASSET_PATH, 'grounded_chat.prompty'), 'utf-8');

interface SearchDocument extends BaseSearchDocument {
  id: string;
  content: string;
  filepath: string;
  title: string;
  url: string;
  contentVector: number[];
}

export async function POST(req: Request) {
  try {
    const { messages } = await req.json();
    console.log('Received messages:', messages);

    if (!messages || !Array.isArray(messages)) {
      throw new Error('Invalid messages format');
    }

    // First, use intent mapping to get better search context
    console.log('Getting chat completions...');
    const intentResponse = await openAIClient.getChatCompletions(
      process.env.AZURE_OPENAI_DEPLOYMENT!,
      [
        { role: 'system', content: intentMappingPrompt },
        ...messages
      ],
      { temperature: 0.3 }
    );
    
    // Log the entire response to see what we're getting
    console.log('Raw Intent Response:', intentResponse);

    // Handle potential undefined response
    if (!intentResponse) {
      throw new Error('No response received from OpenAI');
    }

    // Try to safely access the content
    let searchQuery;
    try {
      searchQuery = intentResponse.choices?.[0]?.message?.content;
      if (!searchQuery) {
        // Fallback to using the last user message as the search query
        const lastUserMessage = messages.findLast(m => m.role === 'user');
        searchQuery = lastUserMessage?.content || '';
        console.log('Using fallback search query:', searchQuery);
      }
    } catch (err) {
      console.error('Error accessing message content:', err);
      // Fallback to using the last user message as the search query
      const lastUserMessage = messages.findLast(m => m.role === 'user');
      searchQuery = lastUserMessage?.content || '';
      console.log('Using fallback search query after error:', searchQuery);
    }

    if (!searchQuery) {
      throw new Error('Could not determine search query');
    }

    console.log('Final Search Query:', searchQuery);

    // Generate embeddings for search
    console.log('Generating embeddings...');
    const embedding = await openAIClient.getEmbeddings(
      process.env.AZURE_OPENAI_DEPLOYMENT!,
      [searchQuery]
    );
    
    if (!embedding?.data?.[0]?.embedding) {
      throw new Error('Invalid embedding response format');
    }

    // Search for relevant documents
    console.log('Searching documents...');
    const searchResults = await searchClient.search('*', {
      filter: '',
      vectorSearchOptions: {
        queries: [{
          kind: 'vector',
          vector: embedding.data[0].embedding,
          kNearestNeighborsCount: 5,
          fields: ["contentVector"]
        }]
      },
      select: ['id', 'content', 'filepath', 'title', 'url']
    });

    const documents = [];
    for await (const result of searchResults.results) {
      const doc = result.document as SearchDocument;
      if (doc) {
        documents.push({
          id: doc.id,
          content: doc.content,
          filepath: doc.filepath,
          title: doc.title,
          url: doc.url
        });
      }
    }
    console.log('Found documents:', documents.length);

    // Generate chat response
    console.log('Generating final chat response...');
    const chatResponse = await openAIClient.getChatCompletions(
      process.env.AZURE_OPENAI_DEPLOYMENT!,
      [
        { 
          role: 'system', 
          content: groundedChatPrompt.replace('{{documents}}', JSON.stringify(documents, null, 2))
        },
        ...messages
      ],
      { 
        temperature: 0.6,
        maxTokens: 1000
      }
    );
    
    // Log the chat response
    console.log('Raw Chat Response:', chatResponse);

    // Handle potential undefined response
    if (!chatResponse) {
      throw new Error('No chat response received from OpenAI');
    }

    const responseContent = chatResponse.choices?.[0]?.message?.content || 'I apologize, but I am unable to provide a response at this time.';

    // Convert the response to a ReadableStream
    const stream = new ReadableStream({
      async start(controller) {
        controller.enqueue(new TextEncoder().encode(responseContent));
        controller.close();
      }
    });

    // Return streaming response
    return new StreamingTextResponse(stream);
  } catch (error: any) {
    console.error('Error in chat endpoint:', {
      message: error.message,
      stack: error.stack,
      name: error.name
    });
    
    return new Response(
      JSON.stringify({ 
        error: 'Internal Server Error', 
        details: error.message,
        stack: process.env.NODE_ENV === 'development' ? error.stack : undefined
      }), 
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      }
    );
  }
} 