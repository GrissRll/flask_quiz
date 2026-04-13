from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "hello world Griss!"





if __name__ == '__main__':
    app.run(debug=True)