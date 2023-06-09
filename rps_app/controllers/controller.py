from flask import Flask, render_template, request, redirect, session
from flask import Blueprint
from models.user import User
from models.game import Game
from repositories import user_repo
from repositories import game_repo
from random import randint

rps_blueprint = Blueprint("rps", __name__)




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
    user = user_repo.select(session["user_id"])
    winner = ""
    game = Game(user, "Computer Player", winner)
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

    
    return render_template('game/play.html', logic = logic, player = player, computer = computer, user = user, game = game)
    

# /users





# @rps_blueprint.route('/user/<id>')
# def show_user(id):
#     user = user_repo.select(id)
#     return render_template('user/show.html', user = user)


# @rps_blueprint.route('/user/opponent', methods=["POST"])
# def show_opponents():
#     users = user_repo.select_all()
#     return render_template('user/show.html', users = users)

