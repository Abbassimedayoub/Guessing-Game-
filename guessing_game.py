import random

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def display_intro(player_name):
    print(f"Welcome to the Guessing game, {player_name}!")
    print("Rules:")
    print("- You will specify an interval.")
    print("- You will then have a limited number of guesses to guess a randomly chosen number within that interval.")
    print("- You win the game if you correctly guess the number within the specified number of attempts.")
    print("- Have fun!\n")

def play_game(player_name):
    # Ask for the minimum and maximum interval
    while True:
        x = get_int("Give me the min of the interval: ")
        y = get_int("Give me the max of the interval: ")
        
        # Check if min > max, switch them if necessary
        if x > y:
            print("Switching min and max values.")
            x, y = y, x
            print(f"The new interval is {x} to {y}\n")
            break
        elif x != y:
            break
        else:
            print("Invalid interval. The maximum must be greater than the minimum.\n")

    # Inform the player about the interval
    print(f"The number to be guessed is in the interval {x} to {y}\n")

    number = random.randint(x, y)

    number_of_guesses = get_int("How many guesses would you like to have? ")
    for attempt in range(number_of_guesses):
        g_number = get_int("What is your guess?\n")
        if g_number < x or g_number > y:
            print("Out of range")
            break
        if g_number == number:
            print(f"Great! The number is {number}. You got it after {attempt + 1} attempts.")
            break
        elif g_number < number:
            print(f"{g_number} is less than the number.")
        else:
            print(f"{g_number} is greater than the number.")
    else:
        print(f"You have exceeded the limit number of attempts. The correct number was {number}")

# Ask for player's name
player_name = input("Welcome to the Guessing game, could you enter your name:\n")
display_intro(player_name)

# Main game loop
while True:
    play_game(player_name)
    replay = input("Do you want to play again? (yes/no)\n")
    if replay.lower() == "no":  # Break the loop if the player does not want to play again
        break
