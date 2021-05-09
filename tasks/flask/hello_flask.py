from flask import  Flask

app = Flask (__name__)

@app.route('/')
def hello() -> str:
    return  'Hello world)'

@app.route('/search4')
def do_search()-> str:
    return 'Search4'

app.run()
