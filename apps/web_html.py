from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Flask Web Server</title>
    </head>
    <body>
        <h1>Welcome to My Simple Web Page</h1>
        <p>This is a simple HTML page served by a Flask web server.</p>
        <p>You can customize this content as you like.</p>
    </body>
    </html>
    '''
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086)
