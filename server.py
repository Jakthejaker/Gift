from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# This route will serve the main index.html file.
@app.route('/')
def home():
    with open(os.path.join('index.html'), 'r') as f:
        html_content = f.read()
    return render_template_string(html_content)

# This route is needed to serve the CSS file
@app.route('/style.css')
def serve_css():
    return send_from_directory(os.getcwd(), 'style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
