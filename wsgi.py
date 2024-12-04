import os
import streamlit.web.bootstrap as bootstrap

def app():
    # Get the app path from where Oryx has extracted it
    app_path = os.getenv('APP_PATH', '/home/site/wwwroot')
    app_file = os.path.join(app_path, 'app.py')
    
    # Run the streamlit app
    bootstrap.run(app_file, "", [], {})

if __name__ == "__main__":
    app() 