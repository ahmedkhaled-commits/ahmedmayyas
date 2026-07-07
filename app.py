from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Test Deploy</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #1a1a1a;
                }
                .emoji {
                    font-size: 200px;
                }
            </style>
        </head>
        <body>
            <div class="emoji">🖕</div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hallo aus dem Docker Container!</h1>"

@app.route("/info")
def info():
    return "<h1>Flask läuft auf AWS EC2 in Docker!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
