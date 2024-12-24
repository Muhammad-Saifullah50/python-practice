# Number guessing game

import random

print("Welcome to my number guessing game")

difficulty_level = input(
    """Select difficulty level number: 
1: Easy
2: Medium
3: Hard \n
"""
)


def compare_numbers(user_data, generated_data):

    hasCompleted = False

    if user_data > generated_data:
        print("Wrong number entered. Please try again with a bit lower number")
        hasCompleted = False

    if user_data < generated_data:
        print("Wrong number entered. Please try again with a higher humber")
        hasCompleted = False

    if user_data == generated_data:
        print("You guessed the correct number")
        hasCompleted = True

    return hasCompleted


def get_consent():

    generate = True

    consent = input("Do you want to continue ?? (y/n): ")

    match consent:
        case "y":
            generate = True

        case "n":
            generate = False

        case _:
            print("Invalid option entered")
            
    return generate

# main function
def guess_game(level):

    if level == "easy":
        generated_number = random.randint(0, 5)

        while True:

            user_input = int(input("Guess the generated number between (0-5): "))
            result = compare_numbers(user_input, generated_number)

            if result != True:
                consent = get_consent()
                if consent == False:
                    print("Thanks for playing, better luck next time")
                    break
                else:
                    continue
            else:
                print("Thank You")
                break

    if level == "medium":
        generated_number = random.randint(0, 10)

        while True:

            user_input = int(input("Guess the generated number between 0-10: "))
            result = compare_numbers(user_input, generated_number)

            if result != True:
                consent = get_consent()
                if consent == False:
                    print("Thanks for playing, better luck next time")
                    break
                else:
                    continue
            else:
                print("Thank You")
                break

    if level == "hard":
        generated_number = random.randint(0, 15)

        while True:

            user_input = int(input("Guess the generated number between (0-15): "))
            result = compare_numbers(user_input, generated_number)

            if result != True:
                consent = get_consent()
                if consent == False:
                    print("Thanks for playing, better luck next time")
                    break
                else:
                    continue
            else:
                print("Thank You")
                break


match difficulty_level:
    case "1":
        guess_game("easy")
    case "2":
        guess_game("medium")
    case "3":
        guess_game("hard")
    case _:
        print("Invalid option entered")
