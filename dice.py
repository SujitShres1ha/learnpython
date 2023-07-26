import random

class Dice:
    def __init__(self):
        pass
    
    def roll(self):
        self.value = random.randint(1,6)
        return self.value
        
class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        
    def update(self,score):
        self.score += score
        
        
def game():
    player1 = input("Enter the name of first player :")
    player2 = input("Enter the name of second player:")
    player1 = Player(player1)
    player2 = Player(player2)
    dice = Dice()

    for _ in range(6):
        x = dice.roll()
        print(player1.name," score: ",x)
        player1.update(x)
        x = dice.roll()
        print(player2.name," score: ",x)
        player2.update(x)

    player1_total = player1.score
    player2_total = player2.score
    print("------Total Scores------")
    print(f"{player1.name} : {player1.score}")
    print(f"{player2.name} : {player2.score}")

    if (player1_total > player2_total):
        print("{} won with {} score".format(player1.name,player1.score))
    elif (player2_total > player1_total):
        print("{} won with {} score".format(player2.name,player2.score))
    else:
        print(f"Game was tied with {player1.score} score")

game()
