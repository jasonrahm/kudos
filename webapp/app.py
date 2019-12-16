from flask import Flask

app = Flask(__name__)
# necessary for unit
# todo determine if rest of app needs the reference
application = app

@app.route('/')
def hello_world():
    return 'Hello World!'

