import secrets

def roulette_game():
    while True:
        # Ask the user to place a bet
        bet_type = input("Place your bet (number, red, black, even, odd): ").lower()
        if bet_type == "number":
            bet_value = int(input("Choose a number between 0 and 36: "))
        else:
            bet_value = None

        # Spin the roulette wheel
        roulette_result = secrets.randbelow(37)
        color_result = "red" if roulette_result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] else "black" if roulette_result != 0 else "green"

        # Display the result of the spin
        print(f"The roulette wheel landed on {color_result} {roulette_result}")

        # Check if the user won
        if bet_type == "number":
            if bet_value == roulette_result:
                print("Congratulations, you won!")
            else:
                print("Sorry, you lost.")
        elif bet_type == color_result:
            print("Congratulations, you won!")
        elif bet_type == "even" and roulette_result % 2 == 0 and roulette_result != 0:
            print("Congratulations, you won!")
        elif bet_type == "odd" and roulette_result % 2 == 1:
            print("Congratulations, you won!")
        else:
            print("Sorry, you lost.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Run the roulette game
roulette_game()
