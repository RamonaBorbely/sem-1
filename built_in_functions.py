# # Task 1
# print('Task 1')
# letter = input("Program Started!\nPlease enter a letter: ")
# print(f"The ASCII code for t is: {ord(letter)}")


# # Task 2
# print('Task 2')
# ascii_code = int(input("Program Started!\nPlease enter an ASCII code: "))
#
# flag = False
# for i in range(32, 127):
#     if i == ascii_code:
#         flag = True
#
# if flag:
#     print(f"The character represented by the ASCII code {ascii_code} is {chr(ascii_code)}.")
# else:
#     print("Error")
# print("Program Ended!")

#
# # Task 3
# print('Task 3')
#
#
# def listen():
#     sound = input("What sound did I hear ?: ")
#     print(f"That was a loud {sound}!")
#
#
# listen()


# # Task 4
# print('Task 4')
#
#
# def identify():
#     user_input = input("What lies before us ?: ").lower()
#     if user_input == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine.")
#
#
# identify()


# # Task 5
# print('Task 5')
#
#
# def escape_by(plan):
#     plan.lower()
#     if plan ==  "jumping over":
#         print("We cannot escape that way! The boulder is too big!")
#     elif plan == "running around":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "going deeper":
#         print("That might just work! Let's go deeper!")
#     else:
#         print("Not sure ...." )
#
#
# escape_by("jumping OVER")
# escape_by("running around")
# escape_by("going deeper")

#
# # Task 6
# print('Task 6')
#
#
# def cross_bridge(distance):
#     if distance > 5:
#         for i in range(distance):
#             print("Crossed step")
#         print("The bridge is collapsing!")
#     else:
#         for i in range(distance):
#             print("Crossed step")
#     print("We must keep going!")
#
#
# cross_bridge(3)
# cross_bridge(6)
#
#
# # # Task 7
# # print('Task 7')
#
#
# def climb_ladder(steps_remaing, steps_crossed):
#     if steps_remaing > steps_crossed:
#         print("Still some way to go!")
#     else:
#         print("We are almost there!")
#
#
# climb_ladder(5, 2)
# climb_ladder(2, 5)


# # Task 8
# print('Task 8')

#
# def display_ladder(steps):
#     for step in range(steps):
#         print("| |\n***")
#
#
# def create_ladder():
#     steps = int(input("How many steps ?: "))
#     display_ladder(steps)
#
#
# create_ladder()


# # Task 9
# print('Task 9')
#
#
# def sum_weights(beep_weight, bop_weight):
#     return beep_weight + bop_weight
#
#
# def calc_avg_weight(beep_weight, bop_weight):
#     return sum_weights(beep_weight, bop_weight) / 2
#
#
# def run():
#     beep = int(input("What is the weight of Beep ?: "))
#     bop = int(input("What is the weight of Bop ?: "))
#     response = input("What would you like to calculate (sum or average) ?: ").lower()
#     if response == "sum":
#         print(sum_weights(beep, bop))
#     elif response == "average":
#         print(calc_avg_weight(beep, bop))
#     else:
#         print("Something went wrong")
#
#
# run()

#
# # Task 10
# print('Task 10')
#
#
# def display_word_in_box(word):
#     print("*********************")
#     print(f"**    {word}      **")
#     print("*********************")
#
#
# def display_word_lower(word):
#     return word.lower()
#
#
# def display_word_upper(word):
#     return word.upper()
#
#
# def display_word_mirrored(word):
#     return word[::-1]
#
#
# def display_alternating_word(word):
#     repeat = int(input("How many times to display the word ?: "))
#     for i in range(repeat):
#         if i % 2 == 0:
#             print(display_word_upper(word))
#         else:
#             print(display_word_lower(word))
#
#
# def run_program():
#     word = input("Enter a word: ")
#     print("""
# 1) Display in a Box – display the word in an ascii art box
# 2) Display Lower-case – display the word in lower-case e.g. hello
# 3) Display Upper-case – display the word in upper-case e.g. HELLO
# 4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
# 5) Repeat – how many times to display the word and then display the word that many times alternating between upper-case
#  and lower-case.
#     """)
#     number = int(input("Choose one number: "))
#     if number == 1:
#         display_word_in_box(word)
#     elif number == 2:
#         print(display_word_lower(word))
#     elif number == 3:
#         print(display_word_upper(word))
#     elif number == 4:
#         print(display_word_mirrored(word))
#     elif number == 5:
#         display_alternating_word(word)
#     else:
#         print("Please enter a number between 1 and 5.")
#
#
# run_program()

# Task 11
print("Task 11")
import random
def play_guess_the_number():
    min_value = int(input("Please enter the minimum value: "))
    max_value = int(input("Please enter the maximum value: "))
    random_number = random.randint(min_value, max_value)
    print(random_number)
    guess = int(input(f"I am thinking of a number between {min_value} and {max_value}. \nCan you guess what it is ?: "))

    while guess != random_number:
        if guess < random_number:
            guess = int(input("To low. Guess again: "))
        else:
            guess = int(input("To high. Guess again: "))
    print("Congratulations! You guessed my number!")


play_guess_the_number()
