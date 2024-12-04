import os
import streamlit.web.bootstrap as bootstrap

def app():
    # Get the app path from environment
    app_path = os.getenv('APP_PATH', '/home/site/wwwroot')
    app_file = os.path.join(app_path, 'app.py')
    
    # Use the PORT environment variable
    port = int(os.getenv('PORT', '8000'))
    
    # Run the streamlit app with the correct port
    bootstrap.run(app_file, "", [f"--server.port={port}", "--server.address=0.0.0.0"], {})

if __name__ == "__main__":
    app() 