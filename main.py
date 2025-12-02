from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Argo CD v1.0!'

app.run(host='0.0.0.0', port=8080)
