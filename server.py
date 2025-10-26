from flask import Flask, render_template_string, send_from_directory
import os

# Get the absolute path of the directory where this script is located
# This makes sure we always find files relative to server.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# This route will serve the main index.html file.
@app.route('/')
def home():
    # Create an absolute path to index.html
    index_path = os.path.join(APP_ROOT, 'index.html')
    with open(index_path, 'r') as f:
        html_content = f.read()
    return render_template_string(html_content)

# This route is needed to serve the CSS file
@app.route('/style.css')
def serve_css():
    # Serve the style.css file from the same directory as this script
    return send_from_directory(APP_ROOT, 'style.css')

if __name__ == '__main__':
    # Render expects the app to bind to 0.0.0.0 and use the PORT env variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)