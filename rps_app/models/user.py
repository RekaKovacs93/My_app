class User:
    def __init__(self, name, wins, losses, ties, id = None):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.id = id