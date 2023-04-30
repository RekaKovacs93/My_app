import pdb

from models.user import User

import repositories.user_repo as user_repo



user1 = User('Samwise Gamgee', 0, 0, 0)
user_repo.save(user1)

user1.losses = 4
user_repo.update(user1)