import random
import time

user_infos_dict = {}
user_checker = []
def game():
    game_point = 100
    print("Let's start with a new number ")
    random_number = random.randint(1, 100)
    while True:

        your_guess = input("Your guess.")
        print(random_number)
        if game_point == 0:
            print("""< Your Point is ZERO >
--------------------------------
----- < Game Over > -----
--------------------------------""")
            menu()
        elif int(your_guess) == random_number:
            print("Congrats you get +25 point")
            game_point += 25
            print("Your point" + str(game_point))
            time.sleep(0.5)
            random_number = random.randint(1,100)

        elif int(your_guess)>random_number*2:
            print("Your guess is too high you will lose 10 point")
            game_point -= 10
            print("Your point" + str(game_point))
            time.sleep(0.5)
            continue
        elif int(your_guess) > random_number and int(your_guess) < random_number*2:
            print("Your guess is  high you will lose 10 point")
            game_point -= 5
            print("Your point" + str(game_point))
            time.sleep(0.5)
            continue
        elif int(your_guess)<random_number/2:
            print("Your guess is too low you will lose 10 point")
            game_point -= 10
            print("Your point" + str(game_point))
            time.sleep(0.5)
            continue
        elif int(your_guess) < random_number and int(your_guess) > random_number/2:
            print("Your guess is  high you will lose 10 point")
            game_point -= 5
            print("Your point" + str(game_point))
            time.sleep(0.5)
            continue

        else:
            print("You entered invalid number")


def login():
    id_input = input("ID:")
    password_input = input("Password:")
    if id_input == user_checker[0] and password_input == user_infos_dict[str(id_input)]:
        print("Welcome" + str(id_input))
        game()


def sing_up():
    sing_up_input = input("Please enter your id.")
    sing_up_input_password = input("Please enter  your password.")
    user_infos_dict[sing_up_input] = sing_up_input_password
    user_checker.append(sing_up_input)

def description():
    return """This project is “ENGR 101 – Introduction to Programming” course’s mini project 01. The
project is a game played by one player by sign up and login system. The player should assume the
randomly generated number and accordingly he/she will earn or lose points."""

def menu():
    while True:
        print("""
--- Welcome to “Guess the Number” Game V.0.3 ---
1. Login
2. Sign Up (Limited to 1 user)
3. Description""")
        menu_input = input("What do you want to do")
        if menu_input == "1":
            if len(user_checker) == 0:
                print("Warning! There is no users :( Please sign up first Going back to main menu...")
                continue
            else:
                login()
        elif menu_input == "2":
            if len(user_checker) == 1:
                print("You can sing only one person")
            else:
                sing_up()
        elif menu_input == "3":
            print(description())
        else:
            print("You entered invalid option.")



menu()