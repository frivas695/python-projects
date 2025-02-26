import random  # Import random module

def guessing_game():
    secret_number = random.randint(1, 100)  # Computer picks a random number
    attempts = 0  # Track number of guesses
    max_attempts = 10  # Limit number of guesses
    best_score = None  # Track best score

    print("🎯 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))  # Get user input
            attempts += 1  

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(f"🏆 New best score: {best_score} attempts!")
                break  # Exit the loop when correct
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Run the game
guessing_game()
