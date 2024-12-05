'use client';

import { useChat } from 'ai/react';
import { useState, useRef, useEffect } from 'react';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Avatar } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Send, Bot, User } from 'lucide-react';
import { Message } from 'ai';
import { nanoid } from 'nanoid';

const WELCOME_MESSAGE: Message = {
  id: nanoid(),
  role: 'assistant',
  content: `👋 Hi there! I'm your enthusiastic RiverTown product specialist, and I'm thrilled to chat with you about our artisanal creations!

Whether you're looking for product recommendations, craftsmanship details, or just want to explore our unique offerings, I'm here to help with warmth and excitement! What would you like to know about?`
};

const QUICK_PROMPTS = [
  "Tell me about your company history",
  "I'd like to design my own ball",
  "Can I speak with customer service?"
];

export default function Home() {
  const [started, setStarted] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    initialMessages: [WELCOME_MESSAGE],
    id: nanoid(),
    onFinish: () => {
      scrollToBottom();
    }
  });

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleQuickPrompt = (prompt: string) => {
    const event = {
      preventDefault: () => {},
      currentTarget: {
        elements: {
          input: { value: prompt }
        }
      }
    } as unknown as React.FormEvent<HTMLFormElement>;
    handleSubmit(event);
    setStarted(true);
  };

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      <header className="sticky top-0 z-50 w-full border-b bg-white/75 dark:bg-gray-900/75 backdrop-blur supports-[backdrop-filter]:bg-white/60">
        <div className="container flex h-16 max-w-screen-2xl items-center px-4">
          <div className="flex items-center gap-3">
            <Bot className="h-8 w-8 text-primary" />
            <span className="font-bold text-xl text-gray-800 dark:text-gray-200">RiverTown Ball Chat</span>
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-hidden py-6">
        <Card className="container max-w-4xl mx-auto h-[calc(100vh-8rem)] flex flex-col bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm">
          <ScrollArea className="flex-1 p-6">
            <div className="space-y-6">
              {messages.map((message) => (
                <div
                  key={message.id}
                  className={`flex items-start gap-4 animate-slideIn ${
                    message.role === 'user' ? 'justify-end' : 'justify-start'
                  }`}
                >
                  {message.role === 'assistant' && (
                    <Avatar className="flex h-10 w-10 shrink-0 overflow-hidden rounded-full ring-2 ring-primary/20">
                      <div className="flex h-full w-full items-center justify-center bg-primary text-white">
                        <Bot className="h-6 w-6" />
                      </div>
                    </Avatar>
                  )}
                  <div
                    className={`relative rounded-2xl px-4 py-3 text-sm shadow-sm ${
                      message.role === 'user'
                        ? 'bg-primary text-primary-foreground ml-auto message-bubble user-message'
                        : 'bg-gray-100 dark:bg-gray-800 mr-auto message-bubble assistant-message'
                    } max-w-[80%]`}
                  >
                    {message.content}
                  </div>
                  {message.role === 'user' && (
                    <Avatar className="flex h-10 w-10 shrink-0 overflow-hidden rounded-full ring-2 ring-primary/20">
                      <div className="flex h-full w-full items-center justify-center bg-gray-200 dark:bg-gray-700">
                        <User className="h-6 w-6 text-gray-600 dark:text-gray-300" />
                      </div>
                    </Avatar>
                  )}
                </div>
              ))}
              <div ref={messagesEndRef} />
            </div>
          </ScrollArea>

          <div className="p-6 border-t bg-white dark:bg-gray-900">
            {!started && (
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
                {QUICK_PROMPTS.map((prompt) => (
                  <Button
                    key={prompt}
                    variant="outline"
                    onClick={() => handleQuickPrompt(prompt)}
                    className="w-full text-sm hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
                  >
                    {prompt}
                  </Button>
                ))}
              </div>
            )}
            <form onSubmit={handleSubmit} className="flex gap-3">
              <Input
                value={input}
                onChange={handleInputChange}
                placeholder="Type your message..."
                className="flex-1 bg-gray-50 dark:bg-gray-800 border-gray-200 dark:border-gray-700 focus:ring-primary/30"
                disabled={isLoading}
              />
              <Button 
                type="submit" 
                disabled={isLoading}
                className="px-4 hover:bg-primary/90 transition-colors"
              >
                <Send className={`h-4 w-4 ${isLoading ? 'animate-pulse' : ''}`} />
              </Button>
            </form>
          </div>
        </Card>
      </main>
    </div>
  );
} 