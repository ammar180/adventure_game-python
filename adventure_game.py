import time
import random

# Function to handle multi-text print with a pause after printing
def print_pause(*text):
    result = ""
    for sup_text in text:
        result += sup_text
    print(result)
    # Pause for 2 seconds after printing
    time.sleep(2)

# Function to validate user input
def get_answer(message, *options):
    ans = input(message)
    # Validate whether the answer is in the valid answer options
    while ans not in options:
        ans = input(message)
    return ans

# Global variable to keep track of the
# total score, enemy, is has new wand
# and the cave is visited or not
global total_score
global enemy
global has_new_wand
global cave_visited

# Function to present the user with the choice of house or cave
def house_or_cave():
    if total_score <= 0:
        return
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    # Get user's choice and validate it
    choice = get_answer("(Please enter 1 or 2).\n", "1", "2")

    # Based on choice, adjust score and call appropriate function
    if choice == "1":
        house()
    if choice == "2":
        cave()

# Function for the cave scenario
def cave():
    global has_new_wand
    global cave_visited
    global total_score

    if not cave_visited:
        total_score += 1
        print_pause(f"Your Total Score Now Is: {total_score}")
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause("You discard your rusty old magic wand",
                    "and take the Wand of Ogoroth with you.")
        has_new_wand = True
        cave_visited = True
    else:
        print_pause(f"Your Total Score Now Is: {total_score}")
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before",
                    ", and gotten all the good stuff.",
                    " It's just an empty cave now.")

    # Present the field's choice again
    print_pause("You walk back out to the field.")
    house_or_cave()

# Function for the house scenario
def house():
    global total_score
    print_pause(f"Your Total Score Now Is: {total_score}")
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens",
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} finds you!")
    if not has_new_wand:
        print_pause("You feel a bit under-prepared for this,",
                    "what with only having a tiny,",
                    " rusty old magic wand.")

    message = "Would you like to (1) cast a spell or (2) run away? "
    choice = get_answer(message, "1", "2")

    # Based on choice, adjust score and call appropriate function
    if choice == "1":
        cast()
    if choice == "2":
        run()

# Function for the spell casting scenario
def cast():
    global total_score

    if has_new_wand:
        total_score += 1
        print_pause(f"Your Total Score Now Is: {total_score}")
        print_pause(f"As the {enemy} moves to cast a spell",
                    " you raise your new Wand of Ogoroth.")
        print_pause("The Wand of Ogoroth shines brightly",
                    " in your hand as you brace yourself for the spell.")
        print_pause(f"But the {enemy} takes one look",
                    " at your shiny new wand and runs away!")
        print_pause(f"You have rid the town of the {enemy}.",
                    " You are victorious!")
    else:
        total_score -= 1
        animal = random.choice(["frog", "mouth", "snake"])
        print_pause(f"Your Total Score Now Is: {total_score}")
        print_pause("You do your best...")
        print_pause("but your rusty old magic wand",
                    f" is no match for the {enemy}.")
        print_pause(f"You have been turned into a {animal}!")

# Function for the running away scenario
def run():
    print_pause(f"Your Total Score Now Is: {total_score}")
    print_pause("You run back into the field.",
                " Luckily, you don't seem to have been followed.")
    # Present the field's choice again
    house_or_cave()

def field():
    # Initial game setup and description
    print_pause(f"Your Initial Total Score Is: {total_score}")
    print_pause("You find yourself standing",
                " in an open field, filled with",
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy",
                " is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)",
                "magic wand.")

# Main game loop
while True:
    #initial value
    total_score = 1
    has_new_wand = False
    cave_visited = False
    enemy = random.choice(["troll", "fairy", "gorgon"])# initial value
    field()

    house_or_cave()

    # End of game summary
    print("\n-----GAME OVER-----\n")

    # Check if the player won or lost
    if total_score > 0:
        print("Congratulations!",
              f"You win the game with a score of ({total_score})")
    else:
        print("Sorry!",
              "You lose the game!")

    # Ask if the player wants to play again
    want_continue = get_answer("Would you like to play again? (y/n)", "y", "n")
    if want_continue == "n":
        print_pause("Thanks for playing! See you next time.")
        break