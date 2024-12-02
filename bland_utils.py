import os
import requests
import logging
import streamlit as st
from settings import BLAND_SCRIPT, CS_NAME_REQUEST, CS_PHONE_REQUEST

# Configure logging
logger = logging.getLogger(__name__)

def init_bland():
    """Initialize Bland API configuration"""
    return {
        'headers': {
            'Authorization': st.secrets["BLAND_API_KEY"]
        },
        'base_url': 'https://us.api.bland.ai/v1'
    }

def extract_phone_number(prompt: str) -> str | None:
    """Extract phone number from prompt using regex"""
    # Clean the input string of any whitespace and common separators
    cleaned_number = ''.join(filter(str.isdigit, prompt))
    
    # If we have exactly 10 digits, assume it's a valid US phone number
    if len(cleaned_number) == 10:
        return f"+1{cleaned_number}"
    
    # If we have 11 digits and it starts with 1, also valid
    if len(cleaned_number) == 11 and cleaned_number.startswith('1'):
        return f"+{cleaned_number}"
    
    # For any other length, return None
    return None

def handle_customer_service_request(prompt: str, phone_number: str = None, customer_name: str = None) -> str | None:
    """Handles customer service related requests and initiates calls if needed"""
    try:
        # List of words that indicate a question rather than a name
        question_words = {
            'what', 'whats', 'when', 'where', 'why', 'how', 'who', 'which', 
            'can', 'could', 'would', 'will', 'does', 'do', 'did', 'is', 'are', 'tell'
        }
        
        # Check if this is a customer service request
        is_cs_request = any(phrase in prompt.lower() for phrase in [
            'speak to someone',
            'talk to a person', 
            'customer service',
            'representative', 
            'speak to a human', 
            'talk to someone',
            'speak with someone',
            'call me back',
            'give me a call',
            'contact me',
            'need help',
            'can someone call',
            'want to speak to',
            'want to talk to',
            'call me'
        ])
        
        # If it starts with a question word or contains question patterns, it's not a CS request
        first_word = prompt.lower().strip().split()[0]
        if first_word in question_words or any(phrase in prompt.lower() for phrase in [
            'company history',
            'tell me about',
            'what is',
            'how does',
            'when was',
            'where is',
            'can you',
            'do you',
            'history',
            'about the',
            'tell us'
        ]):
            return None
        
        is_just_numbers = sum(c.isdigit() for c in prompt) >= 10
        
        # Initial CS request - ask for name first
        if is_cs_request:
            return CS_NAME_REQUEST
        
        # If we don't have a name yet and this isn't a phone number
        if not customer_name and not is_just_numbers and len(prompt.strip()) > 0:
            potential_name = prompt.strip().split()[0]
            # Don't treat common words or short inputs as names
            if (len(potential_name) > 1 and 
                potential_name.lower() not in question_words and 
                not any(c.isdigit() for c in potential_name)):
                # Valid name provided, now ask for phone number
                return CS_PHONE_REQUEST.format(customer_name=potential_name.capitalize())
            return None
        
        # If we have a name but no phone number yet
        if customer_name and not phone_number:
            if is_just_numbers:
                formatted_phone = f"+1{''.join(filter(str.isdigit, prompt))[-10:]}"
                
                # Initiate the call
                data = {
                    "phone_number": formatted_phone,
                    "task": BLAND_SCRIPT.format(customer_name=customer_name),
                    "model": "turbo",
                    "voice": "Alexa",
                    "max_duration": 12,
                    "wait_for_greeting": True,
                    "temperature": 0.8
                }
                
                bland_config = init_bland()
                response = requests.post(
                    f"{bland_config['base_url']}/calls",
                    json=data,
                    headers=bland_config['headers']
                )
                
                if response.status_code == 200:
                    return (f"Perfect! Sara will be calling you right now at " 
                           f"{formatted_phone[-10:-7]}-{formatted_phone[-7:-4]}-{formatted_phone[-4:]}. "
                           f"She's looking forward to helping you with any questions you have about our "
                           f"artisanal wooden balls, {customer_name}!")
                else:
                    logger.error(f"Failed to initiate customer service call: {response.text}")
                    return ("I apologize, but I'm having trouble connecting with Sara at the moment. "
                           "Please try again in a few minutes or call us directly at (719) 266-2837")
            # If we got the name but not a valid phone number yet, ask for the phone number
            return CS_PHONE_REQUEST.format(customer_name=customer_name)
        
        return None
        
    except Exception as e:
        logger.error(f"Error in customer service request handling: {str(e)}", exc_info=True)
        return ("I apologize, but I'm experiencing technical difficulties arranging the call. "
               "Please contact our customer service directly at (719) 266-2837") 