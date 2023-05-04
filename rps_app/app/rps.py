from random import randint

logic = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
}
    

def who_is_the_winner(player, computer):
    if player == computer:
        return "It's a tie"
    elif logic[player] == computer:
        return f"Computer wins, {computer} beats {player}"
    else:
        return f"Player wins, {player} beats {computer}"

 
def converter(num):
    if num == 1:
        return "Rock"
    if num == 2:
        return "Paper"
    if num == 3:
        return "Scissors"

player = input("Select :")
computer = converter(randint(1,3))


print(computer)
print(who_is_the_winner(player, computer))


