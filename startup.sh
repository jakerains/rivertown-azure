#!/bin/bash

# Create .streamlit directory
mkdir -p /root/.streamlit

# Create secrets.toml with environment variables
cat > /root/.streamlit/secrets.toml << EOL
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
echo "Checking environment variables..."
echo "PORT: $PORT"
echo "HTTP_PLATFORM_PORT: $HTTP_PLATFORM_PORT"

# Set Python environment variables
export PYTHONUNBUFFERED=1
export PYTHONPATH=/home/site/wwwroot

# Use PORT from environment variable, fallback to 8000
PORT="${PORT:-${HTTP_PLATFORM_PORT:-8000}}"

# Start Streamlit with dynamic port
cd /home/site/wwwroot
streamlit run app.py \
    --server.port $PORT \
    --server.address 0.0.0.0 \
    --server.maxUploadSize 200 \
    --server.timeout 60 \
    --browser.serverAddress 0.0.0.0 \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false 