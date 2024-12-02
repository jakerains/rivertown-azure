# Rivertown Ball Company Chat Application

## Overview
This Streamlit application provides a user-friendly chat interface for interacting with the Rivertown Ball Company product information system.

## Features
- Real-time chat interface
- Persistent chat history during session
- Context-aware responses
- Product-specific information retrieval
- User-friendly message display
- Centralized settings management

## Technical Implementation
The application is built using:
- Streamlit for the frontend
- Azure AI for chat completions
- Custom prompt templates for response generation
- Session state management for chat history
- Centralized settings in settings.py

## Configuration
All system prompts, UI settings, and model parameters can be configured in `settings.py`. This includes:
- Application title and branding
- UI text and placeholders
- System prompts
- Model parameters (temperature, max tokens, etc.)

## Usage
To run the application:

1. Ensure all requirements are installed:
```bash
pip install -r requirements.txt
```

2. Configure settings in `settings.py` as needed

3. Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```