import os
from flask import Flask

app = Flask(__name__)
version = os.getenv("APP_VERSION", "unknown")
api_key = os.getenv("API_KEY", "missing")

@app.route('/')
def index():
    return f'Hello Argo CD {version}!'

@app.route('/api')
def api():
    return f'{api_key}'

app.run(host='0.0.0.0', port=8080)
