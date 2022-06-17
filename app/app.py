import flask
import sys
from importlib import reload
from flask import request

app = flask.Flask(__name__)

# info for index.html, loaded on GET
BUTTON_NAME = 'button'
ELEM_NAME = 'mtext'
WELCOME_TEXT = 'Hello! Click the button to sort the test text'
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

def sort_lines(lines: str):
    """Sort the lines of text."""
    lines = lines.splitlines()
    new = []
    for item in lines:
        try:
            item.encode('ascii')
        except UnicodeEncodeError:
            continue
        new.append(item)
    return sorted(new)

@app.route('/', methods=['POST'])
def home_post():
    """When the submit is done, we should load this text."""
    new_content = sort_lines(request.form['content'])  # type: str
    return flask.render_template('new.html', content=new_content)

if __name__ == "__main__":
    # leave it on port 5000 for permission sake
    app.run('0.0.0.0', port=5000, debug=True)
