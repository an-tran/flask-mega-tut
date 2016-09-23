# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

#!/home/lavalamp/virtual-env/flask/bin/python

from app import app

app.run(debug=True)