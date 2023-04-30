from flask import Flask, render_template, request, redirect, session
from flask import Blueprint
from models.user import User
from repositories import user_repo
from random import randint

rps_blueprint = Blueprint("rps", __name__)

@rps_blueprint.route('/home')
def home():
    return render_template('index.html')

@rps_blueprint.route('/user/sign_up')
def show_sign_up():
    return render_template('user/sign_up.html')

@rps_blueprint.route('/user/log_in')
def show_log_in():
    users = user_repo.select_all()
    return render_template('user/log_in.html', users = users)

@rps_blueprint.route('/user/', methods=["POST"])
def find_user():
    id = request.form["username"]
    user = user_repo.select(id)
    session["user_id"] = user.id
    return render_template('user/show.html', user = user)


@rps_blueprint.route('/user/profile', methods=["POST"])
def new_user():
    name = request.form["new_username"]
    wins = 0
    losses = 0
    ties = 0
    user = User(name, wins, losses, ties)
    user_repo.save(user)
    session["user_id"] = user.id
    return render_template('/user/show.html', user = user)



@rps_blueprint.route('/game/play')
def play():
    logic = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    user = user_repo.select(session["user_id"])
    return render_template('game/play.html', logic=logic)


@rps_blueprint.route('/game/play', methods=["POST"])
def play_game():
    logic = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
}
    def converter(num):
        if num == 1:
            return "Rock"
        if num == 2:
            return "Paper"
        if num == 3:
            return "Scissors"
    player = request.form["play"]
    computer = converter(randint(1,3))

    if player == computer:
        result = "tie"
    elif logic[player] == computer:
        result = "lose"
    else:
        result = "win"

    user = user_repo.select(session["user_id"])
    if result == "win":
        user.wins += 1
    elif result == "lose":
        user.losses += 1
    else:
        user.ties += 1
    user_repo.update(user)

    
    return render_template('game/play.html', logic = logic, player = player, computer = computer, user = user)
    


@rps_blueprint.route('/user/all_users')
def show_all_users():
    users = user_repo.select_all()
    return render_template('user/all_users.html', users = users)

@rps_blueprint.route('/user/all_users/name')
def show_all_users_by_name():
    users = user_repo.select_all_name()
    return render_template('user/all_users.html', users = users)

@rps_blueprint.route('/user/all_users/wins')
def show_all_users_by_wins():
    users = user_repo.select_all_wins()
    return render_template('user/all_users.html', users = users)

@rps_blueprint.route('/user/all_users/losses')
def show_all_users_by_losses():
    users = user_repo.select_all_losses()
    return render_template('user/all_users.html', users = users)

@rps_blueprint.route('/user/all_users/ties')
def show_all_users_by_ties():
    users = user_repo.select_all_ties()
    return render_template('user/all_users.html', users = users)




# @rps_blueprint.route('/user/<id>')
# def show_user(id):
#     user = user_repo.select(id)
#     return render_template('user/show.html', user = user)


# @rps_blueprint.route('/user/opponent', methods=["POST"])
# def show_opponents():
#     users = user_repo.select_all()
#     return render_template('user/show.html', users = users)

