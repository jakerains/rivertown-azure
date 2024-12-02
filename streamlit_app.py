import streamlit as st
from riverchat import chat_with_products
import os
import time
from dotenv import load_dotenv
from settings import (
    APP_TITLE, 
    APP_ICON, 
    CHAT_INPUT_PLACEHOLDER,
    WELCOME_MESSAGE,
    ASSISTANT_ICON,
    USER_ICON
)

# Load environment variables
load_dotenv()

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Welcome to Rivertown Ball Company! How can I help you today?"
        })
    if "context" not in st.session_state:
        st.session_state.context = {}

def format_response(text):
    """Format the response text with proper spacing and styling"""
    # First, handle lists
    text = text.replace("- ", "\n- ")
    
    # Handle colons
    text = text.replace(": ", ":\n")
    
    # Add paragraph breaks after sentences
    sentences = text.split(". ")
    formatted_sentences = []
    
    for i, sentence in enumerate(sentences):
        if sentence:
            # Add double line break after sentences that end sections
            if any(keyword in sentence.lower() for keyword in ["however", "additionally", "moreover", "in conclusion", "finally"]):
                formatted_sentences.append(sentence + ".\n\n")
            # Add single line break for list items and short sentences
            elif len(sentence) < 50 or sentence.startswith("-"):
                formatted_sentences.append(sentence + ".")
            # Add double line break for longer sentences
            else:
                formatted_sentences.append(sentence + ".\n\n")
    
    text = " ".join(formatted_sentences)
    
    # Clean up any excessive newlines
    text = text.replace("\n\n\n", "\n\n")
    
    # Ensure lists are properly spaced
    text = text.replace("\n-", "\n\n-")
    
    return text.strip()

def display_chat_history():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        icon = ASSISTANT_ICON if message["role"] == "assistant" else USER_ICON
        with st.chat_message(message["role"], avatar=icon):
            st.markdown(format_response(message["content"]))

def stream_response(response_text, message_placeholder):
    """Stream response with natural typing effect"""
    full_response = ""
    # Split into sentences for more natural streaming
    sentences = response_text.split(". ")
    
    for sentence in sentences:
        words = sentence.split()
        for i, word in enumerate(words):
            full_response += word + " "
            # Add period back if it's the last word of the sentence
            if i == len(words) - 1 and sentence != sentences[-1]:
                full_response += ". "
            message_placeholder.markdown(format_response(full_response + "▌"))
            time.sleep(0.05)  # Adjust speed as needed
    
    # Display final response without cursor
    message_placeholder.markdown(format_response(full_response))
    return full_response

def process_user_input():
    """Process user input and generate response"""
    if prompt := st.chat_input("Ask about our wooden balls..."):
        # Display user message
        with st.chat_message("user", avatar=USER_ICON):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get bot response
        with st.chat_message("assistant", avatar=ASSISTANT_ICON):
            message_placeholder = st.empty()
            
            with st.spinner("Crafting the perfect response for you... 🎯"):
                response = chat_with_products(
                    messages=st.session_state.messages,
                    context=st.session_state.context
                )
                
                # Stream the response
                full_response = stream_response(response["message"].content, message_placeholder)
                
                # Update context if needed
                st.session_state.context = response["context"]
                
                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )

def main():
    # Set page config with initial sidebar state
    st.set_page_config(
        page_title="Rivertown Ball Company",
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main {
            background-color: #fef3c7;
            background-image: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
        }
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.8) !important;
            border-radius: 15px !important;
            padding: 20px !important;
            margin: 10px 0 !important;
        }
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.8);
        }
        h1 {
            color: #92400e !important;
            text-align: center;
            padding: 20px 0;
            font-family: 'Arial', sans-serif;
        }
        .stButton > button {
            background-color: #f59e0b;
            color: white;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #d97706;
        }
        /* Style the hamburger menu button */
        button[data-testid="baseButton-header"] {
            background-color: #92400e !important;
            color: white !important;
            padding: 0.5rem !important;
            border-radius: 0.5rem !important;
        }
        button[data-testid="baseButton-header"]:hover {
            background-color: #78350f !important;
        }
        /* Add "Menu" text next to hamburger icon */
        button[data-testid="baseButton-header"]::before {
            content: "Menu ";
            margin-right: 0.5rem;
        }
        /* Improve chat message formatting */
        .stChatMessage p {
            margin-bottom: 1em !important;
            line-height: 1.6 !important;
        }
        .stChatMessage ul {
            margin-top: 0.5em !important;
            margin-bottom: 1em !important;
        }
        .stChatMessage li {
            margin-bottom: 0.5em !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # Header with logo and title
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title(f"{APP_ICON} Rivertown Ball Company")
        st.markdown("""
            <p style='text-align: center; color: #92400e; margin-bottom: 30px;'>
            Crafting Premium Artisanal Balls Since 1985!
            </p>
        """, unsafe_allow_html=True)

    # Create a container for chat messages
    chat_container = st.container()

    # Initialize session state
    initialize_session_state()

    # Display chat history in container
    with chat_container:
        display_chat_history()

    # Handle user input
    process_user_input()

    # Sidebar with reset button and additional info
    with st.sidebar:
        st.markdown("### Chat Controls")
        if st.button("Reset Chat", key="reset"):
            st.session_state.messages = []
            st.session_state.context = {}
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