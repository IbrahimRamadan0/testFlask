from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():  # put application's code here
    return 'Hello World !  1 1 1 !'


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)
