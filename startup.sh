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

# Debug: Print environment variables (remove in production)
echo "Checking environment variables..."
echo "AIPROJECT_CONNECTION_STRING: $AIPROJECT_CONNECTION_STRING"
echo "AISEARCH_INDEX_NAME: $AISEARCH_INDEX_NAME"

# Debug: Check if secrets.toml was created
echo "Checking if secrets.toml exists..."
ls -la /root/.streamlit/

# Start Streamlit
cd /home/site/wwwroot
streamlit run app.py --server.port 8000 --server.address 0.0.0.0 