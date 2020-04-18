import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    """Render a template with the first text and button."""
    return flask.render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    """When the submit is done, we should load this text."""
    return 'New text. Be amazed!'

if __name__ == "__main__":
    # leave it on port 5000 for permission sake
    app.run('0.0.0.0', port=5000, debug=True)