import os
import requests
import logging
from dotenv import load_dotenv
from settings import BLAND_SCRIPT

# Configure logging
logger = logging.getLogger(__name__)

def init_bland():
    """Initialize Bland API configuration"""
    return {
        'headers': {
            'Authorization': os.getenv('BLAND_API_KEY')
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

def handle_customer_service_request(prompt: str, phone_number: str = None) -> str | None:
    """Handles customer service related requests and initiates calls if needed"""
    try:
        # Check if this is a customer service request or just a phone number
        is_cs_request = any(keyword in prompt.lower() for keyword in [
            'speak to someone', 'talk to a person', 'customer service',
            'representative', 'speak to a human', 'talk to someone', 'Being a Karen',   
            'call me', 'contact me'
        ])
        is_just_numbers = sum(c.isdigit() for c in prompt) >= 10
        
        # Initial CS request
        if is_cs_request:
            return ("I'd be happy to have Sara, our customer service specialist, give you a call! "
                   "What's the best phone number to reach you at? You can share it in any format "
                   "like: 123-456-7890 or (123) 456-7890")
        
        # Handle phone number input
        if is_just_numbers:
            formatted_phone = f"+1{''.join(filter(str.isdigit, prompt))[-10:]}"
            
            # Initiate the call
            data = {
                "phone_number": formatted_phone,
                "task": BLAND_SCRIPT,
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
                       "She's looking forward to helping you with any questions you have about our "
                       "artisanal wooden balls!")
            else:
                logger.error(f"Failed to initiate customer service call: {response.text}")
                return ("I apologize, but I'm having trouble connecting with Sara at the moment. "
                       "Please try again in a few minutes or call us directly at (719) 266-2837")
        
        return None
        
    except Exception as e:
        logger.error(f"Error in customer service request handling: {str(e)}", exc_info=True)
        return ("I apologize, but I'm experiencing technical difficulties arranging the call. "
               "Please contact our customer service directly at (719) 266-2837") 