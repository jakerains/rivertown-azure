import os
import streamlit.web.bootstrap as bootstrap

def app():
    # Get the app path from environment or use default
    app_dir = os.getenv('APP_PATH', '/home/site/wwwroot')
    app_file = os.path.join(app_dir, 'app.py')
    
    print(f"Starting Streamlit with app file: {app_file}")
    bootstrap.run(app_file, "", [], {})

if __name__ == "__main__":
    app() 