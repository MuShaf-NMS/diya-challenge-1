from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/web')
def web():
    return """
    <h1 style = "color : red;">halo saya web</h1>
    """

if __name__ == '__main__':
    app.run(debug=True)