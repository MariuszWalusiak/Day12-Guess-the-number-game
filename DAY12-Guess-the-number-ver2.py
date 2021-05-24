import random
print("Welocome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

searched_number = random.randint(0, 100)
print(searched_number)
level_choice = input("Choose a difficulty.Type 'easy' or 'hard'")

    
def guess(attempts):
    should_continue = True
    print(f"You have {attempts} attempts ramaining to guess the number")
    while should_continue and attempts > 0:
        number_choice = int(input("Make a guess"))
        if number_choice == searched_number:
            should_continue = False
            print(f"You got it ! The answer was {searched_number}")
        elif number_choice < searched_number:
            print("Too low")
            if attempts > 1:
                print("Guess again.")
                attempts = attempts - 1
                print(f"You have {attempts} ramaining to guess the number")
            elif attempts == 1:
                should_continue = False
                print("You've run out of guesses, you lose.")
        elif number_choice > searched_number:
            print("Too high")
            if attempts > 1:
                print("Guess again.")
                attempts = attempts - 1
                print(f"You have {attempts} ramaining to guess the number")
            elif attempts == 1:
                should_continue = False
                print("You've run out of guesses, you lose.")


if level_choice == "easy":
    attempts = 10
elif level_choice == "hard":
    attempts = 5

guess(attempts)
