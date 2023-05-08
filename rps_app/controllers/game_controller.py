from flask import Flask, render_template, request, redirect, session
from flask import Blueprint
from models.user import User
from models.game import Game
from repositories import user_repo
from repositories import game_repo
from random import randint

game_blueprint = Blueprint("game", __name__)


@game_blueprint.route('/home')
def home():
    return render_template('index.html')


@game_blueprint.route('/game/show_game')
def play():
    logic = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    user = user_repo.select(session["user_id"])
    return render_template('game/show_game.html', logic=logic)


@game_blueprint.route('/game/play', methods=["POST"])
def play_game():
    user = user_repo.select(session["user_id"])
    winner = ""
    game = Game(user, "Computer", winner)
    game_repo.save(game)
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
    
    
    if result == "win":
        user.wins += 1
        game.winner = user.name
    elif result == "lose":
        game.winner = "Computer"
        user.losses += 1
    else:
        user.ties += 1
        game.winner = "No winner"
    user_repo.update(user)
    game_repo.update(game)

    
    return render_template('game/play.html', logic = logic, player = player, computer = computer,
    user = user, game = game)

@game_blueprint.route('/user/all_users')
def show_all_users():
    users = user_repo.select_all()
    games = game_repo.select_all()
    return render_template('user/all_users.html', users = users, games = games)


# /users?sortBy=name
@game_blueprint.route('/user/all_users/user')
def show_all_users_by_name():
    users = user_repo.select_all()
    games = game_repo.select_all_user()
    return render_template('user/all_users.html', users = users, games = games)

@game_blueprint.route('/user/all_users/opponent')
def show_all_users_by_wins():
    users = user_repo.select_all()
    games = game_repo.select_all_opponent()
    return render_template('user/all_users.html', users = users, games = games)

@game_blueprint.route('/user/all_users/winner')
def show_all_users_by_losses():
    games = game_repo.select_all_winner()
    users = user_repo.select_all()
    return render_template('user/all_users.html', users = users, games = games)
