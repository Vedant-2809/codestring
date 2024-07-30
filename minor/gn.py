import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    attempts = 0
    max_attempts = 5
      # Maximum number of attempts allowed

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number_game()
