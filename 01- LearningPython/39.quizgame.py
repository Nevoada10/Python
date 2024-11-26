# ---------------------------------------------#
def new_game():  # User input

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------------------")
        print(key)
        for option in options[question_num - 1]:
            print(option)
        guess = input("Answer A,B,C,D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# ---------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# ---------------------------------------------#
def display_score(correct_guesses, guesses):
    print("---------------------------------------------")
    print("Results:")
    print("--------------------------------------------")
    print("Answers:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("Score: " + str(int(correct_guesses * 100 / len(questions))) + " %")
    pass


# ---------------------------------------------#
def play_again():
    pass

    response = input("No you want to play again? (Y/N)").upper()
    if response == "Y":
        return True
    else:
        return False


# ---------------------------------------------#

questions = {"Who created Python?: ": "A",
             "What year was Python created?": "B",
             "Python was a tribute to which comedy group?:": "C",
             "Is the Earth round?": "A"}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989 ", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smooch", "C. Monty Python ", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth? "]]

new_game()
while play_again():
    new_game()

print("Program finished.")
