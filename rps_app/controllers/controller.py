from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from repositories import user_repo

rps_blueprint = Blueprint("rps", __name__)

@rps_blueprint.route('/')
def home():
    return render_template('index.html')

@rps_blueprint.route('/user/sign_up')
def show_sign_up():
    return render_template('user/sign_up.html')

@rps_blueprint.route('/user/log_in')
def show_log_in():
    users = user_repo.select_all()
    return render_template('user/log_in.html', users = users)

@rps_blueprint.route('/user/<id>', methods=["POST"])
def find_user(id):
    id = request.form["username"]
    user = user_repo.select(id)
    return render_template('user/show.html', user = user, id = id)


@rps_blueprint.route('/user/sign_up', methods=["POST"])
def new_user():
    name = request.form["username"]
    wins = 0
    losses = 0
    user = User(name, wins, losses)
    user_repo.save(user)
    return redirect('/user/show', user = user)


@rps_blueprint.route('/user/<id>')
def show_user(id):
    user = user_repo.select(id)
    return render_template('user/show.html', user = user)


@rps_blueprint.route('/user/opponent', methods=["POST"])
def show_opponents():
    users = user_repo.select_all()
    return render_template('user/show.html', users = users)



# @rps_blueprint.route("/play")
# def locations():
#     return render_template("play.html")
