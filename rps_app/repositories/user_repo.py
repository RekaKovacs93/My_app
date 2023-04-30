from db.run_sql import run_sql
from models.user import User



def save(user):
    sql = "INSERT INTO users (name, wins, losses, ties) VALUES (%s, %s, %s, %s) RETURNING id"
    values = (user.name, user.wins, user.losses, user.ties)
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
        user = User(result['name'], result['wins'], result['losses'], result['ties'], result['id'] )
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['ties'], row['id'])
        users.append(user)
    return users

def select_all_name():
    users = []

    sql = "SELECT * FROM users ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['ties'], row['id'])
        users.append(user)
    return users

def select_all_wins():
    users = []

    sql = "SELECT * FROM users ORDER BY wins DESC"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['ties'], row['id'])
        users.append(user)
    return users

def select_all_losses():
    users = []

    sql = "SELECT * FROM users ORDER BY losses DESC"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['ties'], row['id'])
        users.append(user)
    return users

def select_all_ties():
    users = []

    sql = "SELECT * FROM users ORDER BY ties DESC"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['wins'], row['losses'], row['ties'], row['id'])
        users.append(user)
    return users

def update(user):
    sql = "UPDATE users SET (name, wins, losses, ties) = (%s, %s, %s, %s) WHERE id = %s"
    values = [user.name, user.wins, user.losses, user.ties, user.id]
    print(f"query: {sql}, values: {values}")
    run_sql(sql, values)