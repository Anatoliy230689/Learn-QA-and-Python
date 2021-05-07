from flask import  Flask

app = Flask (__name__)

@/.route('/')
def hello() -> str:
    return  'Hello world from Flask!'

app.run()
