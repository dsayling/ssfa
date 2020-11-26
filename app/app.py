import flask
from flask import request

app = flask.Flask(__name__)

# info for index.html, loaded on GET
BUTTON_NAME = 'button'
ELEM_NAME = 'mtext'
WELCOME_TEXT = 'Hello! Click for new text'
BUTTON_TEXT = 'Click me!'

# info for new.html, loaded on POST
NEW_TEXT = 'New text. Be amazed!'
NEW_ELEM_NAME = 'new'

@app.route('/')
def home():
    """Render a template with the first text and button."""
    roll = request.args.get('roll')
    output(roll)

@app.route('/', methods=['POST'])
def home_post():
    """When the submit is done, we should load this text."""
    return flask.render_template('new.html',
                                 ntext=NEW_TEXT,
                                 nname=NEW_ELEM_NAME)

import random

#4
def D4():
    roll = random.randint(1,4)
    return roll

# 6
def D6():
    roll = random.randint(1,6)
    return roll

# 8
def D8():
    roll = random.randint(1,8)
    return roll

# 10
def D10():
    roll = random.randint(1,10)
    return roll

# 10 (00-90)
def D00():
    roll = random.randint(1,10)
    return roll

# 12
def D12():
    roll = random.randint(1,12)
    return roll


# 20
def D20():
    roll = random.randint(1,20)
    return roll


# output
dice = {"4":D4,'6':D6,'8':D8, '10':D10, '12':D12, '20':D20}

# I need to figure out how I can just put a command that runs the function a certain amount of times
def output(cmd=None):
    cmd = cmd or input ("Action: ")

    # if the command starts with D, we only want to roll it once
    if cmd.startswith('D'):
        # this splits "D4" into [4], so we want to get the 4 out by index at 0
        die = cmd.split('D')[1]
        # hard code the rollcount to 1
        roll_count = 1
    else:
        # if we get here, the command doesn't start with D, we dont verify that its an integer yet
        roll_count, die = cmd.split('D')
        # the above line splits "3D4" into [3,4] so we want to get the rollcount as index 0, and the die size at index 1

    # get the function that maps to the die size
    die_function = dice.get(die)

    if die_function is None:
        print(f"You dont have a {die} sided die")
        exit(1)

    # run the die function the requested number of rollcounts
    for i in range(int(roll_count)):
        print(die_function())


if __name__ == "__main__":
    # leave it on port 5000 for permission sake
    app.run('0.0.0.0', port=5000, debug=True)
