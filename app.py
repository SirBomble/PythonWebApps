from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def headers():
    return dict(request.headers)

if __name__ == '__main__':
    app.run(debug=True)