from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
	return 'Hello World'

@app.route('/user/<username>')
def user():
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def post80():
	return 'post %d' % post_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
