import pdb

from models.user import User

import repositories.user_repo as user_repo



user1 = User('Samwise Gamgee', 0, 0)
print(user1.__dict__)
user_repo.save(user1)