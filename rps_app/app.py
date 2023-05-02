from flask import Flask, render_template
from controllers.game_controller import *
from controllers.users_controller import *

# from controllers.controller import rps_blueprint
from controllers.users_controller import users_blueprint
from controllers.game_controller import game_blueprint

app = Flask(__name__)
app.secret_key = "Ican"

app.register_blueprint(users_blueprint)
app.register_blueprint(game_blueprint)



if __name__ == '__main__':
    app.run(debug=True)