from flask import Flask
app= Flask(__name__)


@app.route('/')
def index():
    return "<h1>welcome to my app!<h1/>"

@app.route('/<username>')
def user(username):
    return f'<h1>profile for {username}<h1/>'

app.route('/Home')
def home():
    return '<h1>welcome to my home page<h1/>'

if __name__== '__main__':
    app.run(debug=True)