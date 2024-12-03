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
    USER_ICON,
    CS_PHONE_REQUEST
)
from bland_utils import handle_customer_service_request

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
    if "cs_mode" not in st.session_state:
        st.session_state.cs_mode = False
    if "phone_number" not in st.session_state:
        st.session_state.phone_number = None
    if "customer_name" not in st.session_state:
        st.session_state.customer_name = None

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
            
            # Check for customer service request
            cs_response = None
            
            # If we're in CS mode or this is a CS request, handle it
            if st.session_state.cs_mode or any(phrase in prompt.lower() for phrase in [
                'speak to someone', 'talk to a person', 'customer service',
                'representative', 'speak to a human', 'talk to someone',
                'speak with someone', 'call me back', 'give me a call',
                'contact me', 'need help', 'can someone call',
                'want to speak to', 'want to talk to', 'call me'
            ]):
                # Set CS mode if not already set
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
                    # Store the customer's name if it's a valid name response
                    potential_name = prompt.strip().split()[0]
                    if len(potential_name) > 1 and not any(c.isdigit() for c in potential_name):
                        st.session_state.customer_name = potential_name.capitalize()
                        # Force the next response to ask for phone number
                        full_response = stream_response(
                            CS_PHONE_REQUEST.format(customer_name=st.session_state.customer_name), 
                            message_placeholder
                        )
                elif sum(c.isdigit() for c in prompt) >= 10 and st.session_state.customer_name:
                    st.session_state.phone_number = prompt
                    if "sara will be calling you right now" in cs_response.lower():
                        # Keep the name but reset other CS states
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
        /* Force light mode styles */
        [data-testid="stAppViewContainer"], 
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stSidebar"] {
            background: #fcf9f2 !important;
        }
        [data-testid="stMarkdown"] {
            color: #1f2937 !important;
        }
        .main {
            background-color: #fcf9f2;
            background-image: linear-gradient(135deg, #fcf9f2 0%, #fff9ea 100%);
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 15px !important;
            padding: 20px !important;
            margin: 10px 0 !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
            border: 1px solid rgba(0,0,0,0.05) !important;
            max-width: 850px !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(0,0,0,0.1);
            border-radius: 10px;
            padding: 0.75rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            max-width: 850px;
            margin: 0 auto;
        }
        .stTextInput > div > div > input:focus {
            border-color: #f59e0b;
            box-shadow: 0 0 0 2px rgba(245, 158, 11, 0.1);
        }
        h1 {
            color: #92400e !important;
            text-align: center;
            padding: 20px 0;
            font-family: 'Arial', sans-serif;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            margin-bottom: 0.5rem !important;
        }
        /* Style for starter buttons */
        .stButton > button {
            background-color: rgba(245, 158, 11, 0.1);
            color: #92400e;
            border-radius: 12px;
            border: 1px solid rgba(245, 158, 11, 0.2);
            padding: 0.75rem 1.5rem;
            margin: 0.25rem;
            min-width: 200px;
            transition: all 0.2s ease;
            font-size: 0.95rem;
            font-weight: 500;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            backdrop-filter: blur(10px);
        }
        .stButton > button:hover {
            background-color: rgba(245, 158, 11, 0.15);
            border-color: rgba(245, 158, 11, 0.3);
            transform: translateY(-1px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        /* Style the hamburger menu button */
        button[data-testid="baseButton-header"] {
            background-color: rgba(146, 64, 14, 0.1) !important;
            color: #92400e !important;
            padding: 0.5rem !important;
            border-radius: 0.75rem !important;
            border: 1px solid rgba(146, 64, 14, 0.2) !important;
            transition: all 0.2s ease !important;
        }
        button[data-testid="baseButton-header"]:hover {
            background-color: rgba(146, 64, 14, 0.15) !important;
            border-color: rgba(146, 64, 14, 0.3) !important;
        }
        /* Add "Menu" text next to hamburger icon */
        button[data-testid="baseButton-header"]::before {
            content: "Menu ";
            margin-right: 0.5rem;
        }
        /* Improve chat message formatting */
        .stChatMessage p {
            margin-bottom: 1em !important;
            line-height: 1.7 !important;
            color: #1f2937 !important;
            font-size: 1rem !important;
        }
        .stChatMessage ul {
            margin-top: 0.5em !important;
            margin-bottom: 1em !important;
        }
        .stChatMessage li {
            margin-bottom: 0.5em !important;
        }
        /* Force light mode for all elements */
        .stApp {
            background: #fcf9f2 !important;
        }
        .stDeployButton {
            display: none !important;
        }
        .stStatusWidget {
            background: #fcf9f2 !important;
            border: 1px solid rgba(0,0,0,0.05) !important;
        }
        /* Style for starter buttons container */
        div[data-testid="column"] {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .starter-buttons {
            display: flex;
            justify-content: center;
            gap: 0.75rem;
            margin: 2rem auto;
            max-width: 850px;
            padding: 1.5rem;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 16px;
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            backdrop-filter: blur(10px);
        }
        /* Company tagline styling */
        .company-tagline {
            color: #92400e;
            font-size: 1.1rem;
            font-weight: 500;
            text-align: center;
            margin: 1rem 0 2rem;
            letter-spacing: -0.2px;
        }
        /* Chat container styling */
        .chat-container {
            background: rgba(255, 255, 255, 0.5);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            backdrop-filter: blur(10px);
            max-width: 1000px;
            margin: 0 auto;
        }
        /* Spinner styling */
        .stSpinner > div {
            border-color: #f59e0b !important;
            border-bottom-color: transparent !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # Header with logo and title
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title(f"{APP_ICON} Rivertown Ball Company")
        st.markdown("""
            <p class='company-tagline'>
            Crafting Premium Artisanal Balls Since 1985!
            </p>
        """, unsafe_allow_html=True)

    # Create a container for chat messages with styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    chat_container = st.container()

    # Initialize session state
    initialize_session_state()
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    # Display chat history in container
    with chat_container:
        display_chat_history()

    # Add conversation starter buttons (only if not clicked)
    if not st.session_state.button_clicked:
        button_container = st.container()
        with button_container:
            st.markdown('<div class="starter-buttons">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1,1,1])
            
            def send_starter_prompt(prompt):
                st.session_state.button_clicked = True
                if "messages" not in st.session_state:
                    st.session_state.messages = []
                st.session_state.messages.append({"role": "user", "content": prompt})
                # Process the response immediately
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
                st.rerun()

            with col1:
                if st.button("What is the history of Rivertown Ball Company?"):
                    send_starter_prompt("What is the history of Rivertown Ball Company?")
            
            with col2:
                if st.button("How can I design my own ball?"):
                    send_starter_prompt("How can I design my own ball?")
            
            with col3:
                if st.button("Can I have someone call me?"):
                    send_starter_prompt("Can I have someone call me?")
            
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close chat container

    # Handle user input
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
            st.session_state.button_clicked = False
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