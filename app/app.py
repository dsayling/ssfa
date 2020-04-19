import flask

app = flask.Flask(__name__)

# info for index.html, loaded on GET
BUTTON_NAME = 'button'
ELEM_NAME = 'mtext'
WELCOME_TEXT = 'Hello! Click the button for new text'
BUTTON_TEXT = 'Click me!'

# info for new.html, loaded on POST
NEW_TEXT = 'New text. Be amazed!'
NEW_ELEM_NAME = 'new'

@app.route('/')
def home():
    """Render a template with the first text and button."""
    return flask.render_template('index.html',
                                 mtext=WELCOME_TEXT,
                                 mtext_name=ELEM_NAME,
                                 bname=BUTTON_NAME,
                                 btext=BUTTON_TEXT)

@app.route('/', methods=['POST'])
def home_post():
    """When the submit is done, we should load this text."""
    return flask.render_template('new.html',
                                 ntext=NEW_TEXT,
                                 nname=NEW_ELEM_NAME)

if __name__ == "__main__":
    # leave it on port 5000 for permission sake
    app.run('0.0.0.0', port=5000, debug=True)