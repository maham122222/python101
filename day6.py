#Dice Roll Game
#Multiplayer Game

# how to play:
# when its your turn you can roll a dice.When you roll a dice you get a number from 1 to 6.
# if you get any number other than 1 you take that and add that to the score of your turn
# like if you got 5 you have 5 and when roll again and 5 comes then you have 10
# you can decide how many times you want to roll the dice
# when you get 1 , whatever you get on your roll you are done
# whatever you got becaomes zero after 1
# you can roll dice as much as you want, you are gonna decide when to stop
# the person who hits 50 first will win the game

# Breaking down the things
# -allow user to roll the dice
# -ask user if he continue to roll
# -if he stop we will add score to total score
# then check if user score is above 50 if it is then he wins and game ends

import random

def rollDice():
    min_value=1
    max_value=6
    rollDice=random.randint(min_value,max_value)
    return rollDice
# value=rollDice()
# print(value)

while True:
    players=input("Enter the player number between 2 to 4 : ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid enter between 1 to 4")
    else:
        print("Invalid , Try again")

# print(player)
max_score=50
player_score = [0 for _ in range(players)]
while max(player_score)<max_score:
    for i in range(players):
        print('\nPlayer number',i+1,'turn has just started\n')
        print('\n Your total score is : ', player_score[i],'\n')
        current_score=0
        while True:
            roll_again=input("Do you want to roll (y) ? ")
            if roll_again != 'y'.lower():
                break
            value=rollDice()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a : ",value)
       
            print('Your score is ',current_score)
        player_score[i]+=current_score
        print("Your total score : ",current_score)

max_score = max(player_score)
winning=player_score.index[max_score]
print("Player number",winning+1, 'is the winner with a score of ',max_score )





















