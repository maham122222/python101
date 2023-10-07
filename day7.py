# question answers game

def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter (A , B, C or D ): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)

        question_num+=1
    display_score(correct_guesses,guesses)
def check_answer(answers,guess):
    if answers == guess:
        print("correct")
        return 1
    else:
        print("Wrong")
        return 0
    
def display_score(correct_guesses,guesses):
    print("----------------")
    print("Results")
    print("----------------")
    print("Answers", end="")
    for i in questions:
        print(questions.get(i),end= "")
        print("")

    print("Guesses", end=" ")
    for i in guesses:
        print((i),end="")
        print("")

    score=int((correct_guesses/len(questions))*100)
    print("Your score is "+ str(score)+"%")




    
def play_again():
    response = input("Do you want to play again (yes or no ): ? ")
    response=response.upper()

    if response == 'YES':
        return True
    else:
        return False


# Questions
questions={ 
'What is the chemical symbol of water ?' : 'B',
'Which gas do plants absorb from the atmosphere during photosynthesis ?': 'B'
,
'What is the largest planet in our solar system ? ': 'C',
"Is the earth round ? ": 'A'

}

options=[["A . H3O","B . H2O", "C . HCO4"],
         ["A . CO87", "B . CO2", "C . CO3"],
         ["A . Mars", "B . Venus", "C . Jupitar"],
         ["A . True", "B . False", "C . Sometimes"]

]

new_game()

while play_again():
    new_game()

print("bye!")


