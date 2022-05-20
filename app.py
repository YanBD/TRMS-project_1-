from flask import Flask
from flask_cors import CORS
from controllers import front_controller as front
app = Flask(__name__)
cors = CORS(app)
front.route(app)


if __name__ == '__main__':
    app.run()
