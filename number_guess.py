import random

def number_guessing_game():
    # Set the range for the random number
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}.")

    attempts = 0
    while True:
        try:
            player_guess = int(input("Take a guess: "))
            attempts += 1

            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
