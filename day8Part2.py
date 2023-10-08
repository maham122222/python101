# hangman game
import random
list = ['apple','mango']

def game():
    value = random.choice(list)

    display=[]

    for i in range(len(value)):
        display+='-'

    print(display)
    lives=6
    game_over=False
    while not game_over:
        guess=input("enter guess ").lower()

        for position in range(len(value)):
            letter=value[position]
            if letter == guess:
                display[position]=guess

        print(display)
        if guess not in value:
            lives -= -1
            if lives == 0:
                print('you lose')

        if '-' not in display:
            game_over=True
            print('you win')


def play_again():
    again=input('Do you want to play again (yes or no): ')
    if again.lower()=='yes':
        return True
    else:
        return False

game()
while play_again():
    game()
    


    


