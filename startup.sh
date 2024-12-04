#!/bin/bash

# Debug: Print current directory and script location
echo "Startup script location: $0"
echo "Current directory: $(pwd)"

# Ensure startup script is in the correct location
if [ "$0" != "/opt/startup/startup.sh" ]; then
    echo "Copying startup script to /opt/startup/"
    mkdir -p /opt/startup
    cp "$0" /opt/startup/startup.sh
    chmod +x /opt/startup/startup.sh
fi

# Determine the app directory (try tmp first, fall back to wwwroot)
APP_DIR=$(find /tmp -name "app.py" -exec dirname {} \; 2>/dev/null || echo "/home/site/wwwroot")
echo "Using app directory: $APP_DIR"

# Create .streamlit directory in the app directory
mkdir -p "$APP_DIR/.streamlit"

# Create secrets.toml with environment variables
cat > "$APP_DIR/.streamlit/secrets.toml" << EOL
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

# Use PORT from environment variables with fallbacks
PORT="${PORT:-${HTTP_PLATFORM_PORT:-${WEBSITES_PORT:-8000}}}"
echo "Using port: $PORT"

# Change to the app directory
cd "$APP_DIR"

# Start Streamlit
streamlit run app.py --server.port $PORT --server.address 0.0.0.0