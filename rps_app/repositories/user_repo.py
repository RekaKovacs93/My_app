from db.run_sql import run_sql
from models.user import User



def save(user):
    sql = "INSERT INTO users (name, wins, losses) VALUES (%s, %s, %s) RETURNING id"
    values = (user.name, user.wins, user.losses)
    results = run_sql(sql, values)
    user.id = results[0]["id"]
    return user

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result['name'], result['wins'], result['losses'], result['id'] )
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['id'])
        users.append(user)
    return users