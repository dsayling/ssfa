# Super Simple Flask App

AKA.... ssfa

(who doesn't love another acronym...?)

## Manual Env Setup

### Setup the env

You could use a python virtualenv or dockercontainer, but this assumes you have python3 setup with proper dev tools installed (like pip, setuptools, and wheel). You may need to use `pip3` if not mapped to `/usr/bin/pip`.

```
git clone <repo>
cd ssfa
pip install -r requirements.txt
```

### Run the app

Run the app, by default it runs on localhost:5000 and in debug mode. This is currently not configurable.
You may need to use `python3` if not mapped to `/usr/bin/python`.

```
python app.py
```

### Run the tests

Get the drivers for chrome for your distro
https://chromedriver.chromium.org/downloads

```
cd tests/
python -m unittest
```

Currently there are two expected failures.
The assert false test case and the firefox test case.
