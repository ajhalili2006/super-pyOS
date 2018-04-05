from os import environ

from flask import Flask, render_template
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template('index.html')
    #return "<h1 style='color:blue'>Hello There!</h1>"

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(environ['PORT']))