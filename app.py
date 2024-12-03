import streamlit as st
from riverchat import chat_with_products
import time
from settings import (
    APP_TITLE, 
    APP_ICON, 
    CHAT_INPUT_PLACEHOLDER,
    WELCOME_MESSAGE,
    ASSISTANT_ICON,
    USER_ICON,
    CS_PHONE_REQUEST
)
from bland_utils import handle_customer_service_request

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Welcome to Rivertown Ball Company! How can I help you today?"
        })
    if "chat_started" not in st.session_state:
        st.session_state.chat_started = False
    if "context" not in st.session_state:
        st.session_state.context = {}
    if "cs_mode" not in st.session_state:
        st.session_state.cs_mode = False
    if "phone_number" not in st.session_state:
        st.session_state.phone_number = None
    if "customer_name" not in st.session_state:
        st.session_state.customer_name = None

def format_response(text):
    """Format the response text with proper spacing and styling"""
    # Handle lists first
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.strip().startswith('- '):
            formatted_lines.append(line)
        else:
            # Split non-list text into sentences
            sentences = line.split('. ')
            formatted_sentences = []
            
            for i, sentence in enumerate(sentences):
                if not sentence.strip():
                    continue
                    
                sentence = sentence.strip()
                
                # Add period back if it's not the last sentence
                if i < len(sentences) - 1:
                    sentence += '.'
                
                # Add double line break for transition words
                if any(keyword in sentence.lower() for keyword in 
                      ['however', 'additionally', 'moreover', 
                       'in conclusion', 'finally', 'furthermore']):
                    sentence += '\n\n'
                # Add single line break for shorter sentences
                elif len(sentence) < 50:
                    sentence += '\n'
                # Add double line break for longer sentences
                else:
                    sentence += '\n\n'
                    
                formatted_sentences.append(sentence)
            
            formatted_lines.extend(formatted_sentences)
    
    # Join everything back together
    text = ' '.join(formatted_lines)
    
    # Clean up spacing
    text = text.replace('\n \n', '\n\n')
    text = text.replace('\n\n\n', '\n\n')
    text = text.replace('.\n', '.\n\n')
    text = text.replace(':\n', ':\n\n')
    
    # Ensure proper spacing around lists
    text = text.replace('\n- ', '\n\n- ')
    
    return text.strip()

def display_chat_history():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        icon = ASSISTANT_ICON if message["role"] == "assistant" else USER_ICON
        with st.chat_message(message["role"], avatar=icon):
            st.markdown(format_response(message["content"]))

def stream_response(response_text, message_placeholder):
    """Stream response with natural typing effect"""
    # Don't initialize with empty message as it might cause formatting issues
    full_response = ""
    
    for char in response_text:
        full_response += char
        message_placeholder.markdown(full_response + "▌")
        time.sleep(0.02)
    
    # Final display without cursor
    message_placeholder.markdown(full_response)
    return full_response

def process_user_input():
    """Process user input and generate response"""
    if prompt := st.chat_input("Ask about our wooden balls..."):
        # Display user message
        with st.chat_message("user", avatar=USER_ICON):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get bot response - SINGLE message container
        with st.chat_message("assistant", avatar=ASSISTANT_ICON):
            message_placeholder = st.empty()
            
            # Check for customer service request ONCE
            if st.session_state.cs_mode or any(phrase in prompt.lower() for phrase in [
                'speak to someone', 'talk to a person', 'customer service',
                'representative', 'speak to a human', 'talk to someone',
                'speak with someone', 'call me back', 'give me a call',
                'contact me', 'need help', 'can someone call',
                'want to speak to', 'want to talk to', 'call me'
            ]):
                if not st.session_state.cs_mode:
                    st.session_state.cs_mode = True
                
                cs_response = handle_customer_service_request(
                    prompt, 
                    st.session_state.phone_number,
                    st.session_state.customer_name
                )
                
                # Stream response ONCE
                full_response = stream_response(cs_response, message_placeholder)
                
                # Update state ONCE
                if "could you share your first name" in cs_response.lower():
                    st.session_state.customer_name = None
                elif st.session_state.cs_mode and not st.session_state.customer_name:
                    potential_name = prompt.strip().split()[0]
                    if len(potential_name) > 1 and not any(c.isdigit() for c in potential_name):
                        st.session_state.customer_name = potential_name.capitalize()
                        full_response = CS_PHONE_REQUEST.format(customer_name=st.session_state.customer_name)
                        message_placeholder.markdown(full_response)
                elif sum(c.isdigit() for c in prompt) >= 10 and st.session_state.customer_name:
                    st.session_state.phone_number = prompt
                    if "sara will be calling you right now" in cs_response.lower():
                        st.session_state.cs_mode = False
                        st.session_state.phone_number = None
                
                # Add to history ONCE
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )
            else:
                # Regular chat response
                loading_placeholder = st.empty()
                with loading_placeholder:
                    with st.spinner("Crafting the perfect response for you... 🎯"):
                        response = chat_with_products(
                            messages=st.session_state.messages,
                            context=st.session_state.context
                        )
                loading_placeholder.empty()
                
                # Stream response ONCE
                full_response = stream_response(response["message"].content, message_placeholder)
                
                # Update context if needed
                st.session_state.context = response["context"]
                
                # Add to history ONCE
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )

def main():
    # Set page config to hide the streamlit header and menu
    st.set_page_config(
        page_title="Rivertown Ball Company",
        page_icon="🟤",
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={},  # Empty dict removes all menu items
    )
    
    # Hide streamlit elements including the top bar
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

    # Update the CSS section to modify message alignment
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: #eae0d5;  /* Darker warm background */
        }
        
        /* Chat message container */
        .stChatMessage {
            background-color: white !important;
            border-radius: 20px !important;
            padding: 1.5rem !important;
            max-width: 85% !important;
            margin: 1rem 0 !important;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08) !important;
            border: 1px solid rgba(146, 64, 14, 0.1) !important;
            transition: all 0.2s ease !important;
        }
        
        /* User message styling */
        .stChatMessage[data-testid="user-message"] {
            background-color: #92400e !important;  /* Rich wood brown */
            color: white !important;
        }
        
        /* Assistant message styling */
        .stChatMessage[data-testid="assistant-message"] {
            background-color: white !important;
            border: 1px solid rgba(146, 64, 14, 0.2) !important;
        }
        
        /* Avatar styling */
        .stChatMessage .stAvatar {
            width: 35px !important;
            height: 35px !important;
            margin: 0 10px !important;
            border: 2px solid rgba(146, 64, 14, 0.2) !important;
            border-radius: 50% !important;
        }
        
        /* Chat input styling */
        .stChatInput {
            border-color: rgba(146, 64, 14, 0.2) !important;
            padding: 0.5rem !important;
        }
        
        /* Header styling */
        [data-testid="stHeader"] {
            background-color: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
        }

        /* Button styling */
        .stButton > button {
            background-color: #92400e !important;
            color: white !important;
            border: none !important;
            padding: 0.5rem 1rem !important;
            border-radius: 10px !important;
            font-weight: 500 !important;
            transition: all 0.2s ease !important;
        }
        
        .stButton > button:hover {
            background-color: #7c3710 !important;
            box-shadow: 0 2px 8px rgba(146, 64, 14, 0.2) !important;
        }

        /* Message text styling */
        .stMarkdown {
            line-height: 1.5 !important;
        }
        
        /* Improve spacing between messages */
        .stChatMessage + .stChatMessage {
            margin-top: 1.5rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add the header with improved styling
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0; background: rgba(255,255,255,0.5); border-radius: 20px; margin-bottom: 2rem; backdrop-filter: blur(10px);'>
            <h1 style='margin: 0; padding: 0.5rem 0;'>🟤 RiverTown Ball Customer Chat</h1>
            <p style='color: #92400e; font-size: 1.1rem; margin: 0; padding-bottom: 0.5rem;'>Crafting Premium Artisanal Balls Since 1985!</p>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    initialize_session_state()
    
    # Create a container for chat messages with styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    chat_container = st.container()

    # Display chat history in container
    with chat_container:
        display_chat_history()

    st.markdown('</div>', unsafe_allow_html=True)  # Close chat container

    # Create columns for the buttons
    if not st.session_state.chat_started:
        col1, col2, col3 = st.columns(3)
        
        # Define button click handlers
        def handle_button_click(text):
            st.session_state.chat_started = True
            st.session_state.current_input = text
            st.rerun()  # Force rerun to update UI
            
        with col1:
            if st.button("Company History", key="history_btn"):
                handle_button_click("What is the history of Rivertown Ball Company?")
                
        with col2:
            if st.button("Design My Ball", key="design_btn"):
                handle_button_click("How can I design my own ball?")
                
        with col3:
            if st.button("Request Call", key="call_btn"):
                handle_button_click("Can I have someone call me?")

    # Modify process_user_input to handle button inputs
    if "current_input" in st.session_state:
        prompt = st.session_state.current_input
        del st.session_state.current_input
        
        # Display user message
        with st.chat_message("user", avatar=USER_ICON):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get bot response
        with st.chat_message("assistant", avatar=ASSISTANT_ICON):
            message_placeholder = st.empty()
            
            # Check for customer service request
            cs_response = None
            
            if st.session_state.cs_mode or any(phrase in prompt.lower() for phrase in [
                'speak to someone', 'talk to a person', 'customer service',
                'representative', 'speak to a human', 'talk to someone',
                'speak with someone', 'call me back', 'give me a call',
                'contact me', 'need help', 'can someone call',
                'want to speak to', 'want to talk to', 'call me'
            ]):
                if not st.session_state.cs_mode:
                    st.session_state.cs_mode = True
                
                cs_response = handle_customer_service_request(
                    prompt, 
                    st.session_state.phone_number,
                    st.session_state.customer_name
                )
            
            if cs_response:
                # Stream the customer service response
                full_response = stream_response(cs_response, message_placeholder)
                
                # Update session state based on response
                if "could you share your first name" in cs_response.lower():
                    st.session_state.customer_name = None
                elif st.session_state.cs_mode and not st.session_state.customer_name:
                    potential_name = prompt.strip().split()[0]
                    if len(potential_name) > 1 and not any(c.isdigit() for c in potential_name):
                        st.session_state.customer_name = potential_name.capitalize()
                        # Add the current response to chat history
                        st.session_state.messages.append(
                            {"role": "assistant", "content": full_response}
                        )
                        # Instead of creating a new chat message, update the placeholder
                        full_response = CS_PHONE_REQUEST.format(customer_name=st.session_state.customer_name)
                        stream_response(full_response, message_placeholder)
                elif sum(c.isdigit() for c in prompt) >= 10 and st.session_state.customer_name:
                    st.session_state.phone_number = prompt
                    if "sara will be calling you right now" in cs_response.lower():
                        st.session_state.cs_mode = False
                        st.session_state.phone_number = None
            else:
                # Regular chat response
                loading_placeholder = st.empty()
                with loading_placeholder:
                    with st.spinner("Crafting the perfect response for you... 🎯"):
                        response = chat_with_products(
                            messages=st.session_state.messages,
                            context=st.session_state.context
                        )
                # Clear the loading message before streaming
                loading_placeholder.empty()
                
                # Stream the response
                full_response = stream_response(response["message"].content, message_placeholder)
                
                # Update context if needed
                st.session_state.context = response["context"]
            
            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )

    # Regular chat input processing
    process_user_input()

    # Sidebar with reset button and additional info
    with st.sidebar:
        st.markdown("### Chat Controls")
        if st.button("Reset Chat", key="reset"):
            st.session_state.messages = []
            st.session_state.context = {}
            st.session_state.cs_mode = False
            st.session_state.phone_number = None
            st.session_state.customer_name = None
            st.session_state.chat_started = False  # Reset chat started state
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
            ### About Us
            Rivertown Ball Company has been crafting premium wooden balls 
            since 1985. Our commitment to quality and craftsmanship 
            makes us the leading choice for wooden ball products.
        """)

if __name__ == "__main__":
    main() 