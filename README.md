# Super Simple Flask App

AKA.... **ssfa**

(who doesn't love another acronym...?)

## Manual Env Setup

### Setup the env

You could use a python virtualenv or dockercontainer, but this assumes you have python3 setup with proper dev tools installed (like pip, setuptools, and wheel). You may need to use `pip3` if not linked to `/usr/bin/pip`.

```
git clone https://github.com/dsayling/ssfa
cd ssfa
pip install -r requirements.txt  # installs flask and gunicorn
```

### Run the app

Run the app, by default it runs on http://localhost:5000 and in debug mode. This is currently not configurable.
You may need to use `python3` if not linked to `/usr/bin/python`.

```
python app.py
```

### Run the tests

Get the `chromedriver` for your distro
https://chromedriver.chromium.org/downloads
Ensure it's in the `$PATH`

```
cd tests/
pip install -r requirements.txt  # installs selenium
python -m unittest
```

Currently there are two expected failures.
The assert false test case and the firefox test case.
