#!/bin/bash

# Debug: Print current directory and contents
echo "Current directory: $(pwd)"
echo "Directory contents:"
ls -la

# Create .streamlit directory in the correct location
mkdir -p /tmp/8dd148eac327cff/.streamlit

# Create secrets.toml with environment variables
cat > /tmp/8dd148eac327cff/.streamlit/secrets.toml << EOL
# Azure AI Project Connection
AIPROJECT_CONNECTION_STRING = "$AIPROJECT_CONNECTION_STRING"

# Azure Search Configuration
AISEARCH_INDEX_NAME = "$AISEARCH_INDEX_NAME"
AISEARCH_ENDPOINT = "$AISEARCH_ENDPOINT"
AISEARCH_KEY = "$AISEARCH_KEY"

# Model Settings
EMBEDDINGS_MODEL = "$EMBEDDINGS_MODEL"
INTENT_MAPPING_MODEL = "$INTENT_MAPPING_MODEL"
CHAT_MODEL = "$CHAT_MODEL"
EVALUATION_MODEL = "$EVALUATION_MODEL"

# Bland AI
BLAND_API_KEY = "$BLAND_API_KEY"
EOL

# Debug: Print environment variables
echo "Checking port configuration..."
echo "PORT: $PORT"
echo "HTTP_PLATFORM_PORT: $HTTP_PLATFORM_PORT"
echo "WEBSITES_PORT: $WEBSITES_PORT"

# Use PORT from environment variables with fallbacks
PORT="${PORT:-${HTTP_PLATFORM_PORT:-${WEBSITES_PORT:-8000}}}"
echo "Using port: $PORT"

# Add after line 6
echo "Startup script location: $0"
echo "Working directory: $PWD"

# Start Streamlit
cd /tmp/8dd148eac327cff
streamlit run app.py --server.port $PORT --server.address 0.0.0.0