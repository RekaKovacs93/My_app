from db.run_sql import run_sql
from models.user import User
from models.game import Game
from repositories import user_repo



def save(game):
    sql = "INSERT INTO games (user_id, opponent, winner) VALUES (%s, %s, %s) RETURNING id"
    values = (game.user.id, game.opponent, game.winner)
    results = run_sql(sql, values)
    game.id = results[0]["id"]
    return game

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = user_repo.select(result['user_id'])
        game = Game(user, result['opponent'], result['winner'], result['id'] )
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select(row['user_id'])
        game = Game(user, row['opponent'], row['winner'], row['id'])
        games.append(game)
    return games

def select_all_user():
    games = []

    sql = "SELECT * FROM games ORDER BY user ASC"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select(row['user_id'])
        game = Game(user, row['opponent'], row['winner'], row['id'])
        games.append(game)
    return games

def select_all_opponent():
    games = []

    sql = "SELECT * FROM games ORDER BY opponent ASC"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select(row['user_id'])
        game = Game(user, row['opponent'], row['winner'], row['id'])
        games.append(game)
    return games

def select_all_winner():
    games = []

    sql = "SELECT * FROM games ORDER BY winner ASC"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select(row['user_id'])
        game = Game(user, row['opponent'], row['winner'], row['id'])
        games.append(game)
    return games

def update(game):
    sql = "UPDATE games SET (user_id, opponent, winner) = (%s, %s, %s) WHERE id = %s"
    values = [game.user.id, game.opponent, game.winner, game.id]
    run_sql(sql, values)

# def update_scores