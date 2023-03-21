from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Python microservice!"




if __name__ == '__main__':
    context = ('ssl/cert.pem', 'ssl/key.pem') # SSL/TLS certificates and keys
    app.run(host='0.0.0.0', port=9977, ssl_context=context)