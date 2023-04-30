from flask import Flask, render_template

from controllers.controller import rps_blueprint

app = Flask(__name__)

app.register_blueprint(rps_blueprint)



if __name__ == '__main__':
    app.run(debug=True)