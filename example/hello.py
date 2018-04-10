from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

if __name__ == '__main__':
    app.run(debug=True)