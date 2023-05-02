from flask import Flask, render_template, request, redirect, session
from flask import Blueprint
from models.user import User
from models.game import Game
from repositories import user_repo
from repositories import game_repo
from random import randint

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route('/user/sign_up')
def show_sign_up():
    return render_template('user/sign_up.html')

@users_blueprint.route('/user/log_in')
def show_log_in():
    users = user_repo.select_all()
    return render_template('user/log_in.html', users = users)

@users_blueprint.route('/user/', methods=["POST"])
def find_user():
    id = request.form["username"]
    user = user_repo.select(id)
    session["user_id"] = user.id
    return render_template('user/show.html', user = user)


@users_blueprint.route('/user/profile', methods=["POST"])
def new_user():
    name = request.form["new_username"]
    wins = 0
    losses = 0
    ties = 0
    user = User(name, wins, losses, ties)
    user_repo.save(user)
    session["user_id"] = user.id
    return render_template('/user/show.html', user = user)

@users_blueprint.route('/user/all_users')
def show_all_users():
    users = user_repo.select_all()
    games = game_repo.select_all()
    return render_template('user/all_users.html', users = users, games = games)


# /users?sortBy=name
@users_blueprint.route('/user/all_users/name')
def show_all_users_by_name():
    users = user_repo.select_all_name()
    games = game_repo.select_all()
    return render_template('user/all_users.html', users = users, games = games)

@users_blueprint.route('/user/all_users/wins')
def show_all_users_by_wins():
    users = user_repo.select_all_wins()
    games = game_repo.select_all()
    return render_template('user/all_users.html', users = users, games = games)

@users_blueprint.route('/user/all_users/losses')
def show_all_users_by_losses():
    games = game_repo.select_all()
    users = user_repo.select_all_losses()
    return render_template('user/all_users.html', users = users, games = games)

@users_blueprint.route('/user/all_users/ties')
def show_all_users_by_ties():
    users = user_repo.select_all_ties()
    games = game_repo.select_all
    return render_template('user/all_users.html', users = users, games = games)