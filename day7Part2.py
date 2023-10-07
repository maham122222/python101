#Guess the number
import random
def guess_number():
    randomm = random.randint(1,100)

    player_guess_counter=0

    while True:
        guess = int(input("Enter the number between 1 and 100 : "))

        if guess == randomm:
            print("correct")
        elif guess > randomm:
            print("Too high! Try again")
        elif guess < randomm:
            print("To low! Try again")

def play_again():
    again=input("Do you want to play again (yes or no) : ")
    if again.lower() == 'yes':
        return True
    else:
        print("Bye!")
        return False
    
guess_number()
    
while play_again():
    guess_number()

