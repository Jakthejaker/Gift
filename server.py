from flask import Flask, render_template, send_from_directory
import os

# Get the absolute path of the directory where this script is located
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Tell Flask that our 'templates' (index.html) and
# 'static' files (style.css) are in this SAME directory.
app = Flask(__name__,
            template_folder=APP_ROOT,
            static_folder=APP_ROOT)

@app.route('/')
def home():
    # 'render_template' will now correctly look for 'index.html'
    # in the 'template_folder' we defined above (which is APP_ROOT)
    return render_template('index.html')

@app.route('/style.css')
def serve_css():
    # This will correctly serve 'style.css' from the
    # 'static_folder' we defined above (which is APP_ROOT)
    return send_from_directory(app.static_folder, 'style.css')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)