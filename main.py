# NOTES ABOUT FILE
#
# Function: main.py is the runner python file for this webapp
# About: 
# - uses flask
# - runs the app(created from __init__.py) and ensures the app is being run from main.py as opposed #   to an external file importing main.py
# 
#

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
