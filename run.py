from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    now = datetime.utcnow()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

if __name__ == '__main__':
 app.run(host='0.0.0.0',
        port=8080,
        debug=True)
