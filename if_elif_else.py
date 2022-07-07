# Activity 1
print("ACTIVITY 1")
answer = input("What type of book is this?: ")
if answer.lower() == "adventure":
    print("I like adventure books!")

print("Finished reading book.")


# Activity 2
print("ACTIVITY 2")
answer_2 = input("Please enter the activity to be performed:")
if answer_2.lower() == "calculate":
    print("Performing calculations...")

print("Activity completed!")


# Activity 3
print("ACTIVITY 3")
answer_3 = input("Towards which direction should I paint (up, down, left or right)?").lower()
if answer_3 == "up" or answer_3 == "down" or answer_3 == "left" or answer_3 == "right":
    print(f"I am painting in the {answer_3} direction")


# Activity 4
print("ACTIVITY 4")
answer_4 = int(input("Please enter a whole number:"))
if answer_4 % 2 == 0:
    print(f"The number {answer_4} is an even number.")
else:
    print(f"The number {answer_4} is an odd number.")


# Activity 5
print("ACTIVITY 5")
number_one = int(input("Please enter the first number: "))
number_two = int(input("Please enter the second number: "))
if number_one < number_two:
    print("First number is smaller.")
else:
    print("Second number is smaller.")


# Activity 6
print("ACTIVITY 6")
n1 = int(input("Please enter the first whole number: "))
n2 = int(input("Please enter the second whole number: "))
n3 = int(input("Please enter the third whole number: "))


count_even = 0
count_odd = 0

if n1 % 2 == 0:
    count_even +=1
else:
    count_odd +=1

if n2 % 2 == 0:
    count_even +=1
else:
    count_odd +=1

if n3 % 2 == 0:
    count_even +=1
else:
    count_odd +=1

print(f"There were {count_even} even and {count_odd} odd numbers.")

# Activity 6 using a list
print("ACTIVITY 6 USING LIST")
numbers = []
odd_numbers = 0
even_numbers = 0

reading = True
while reading:
    new_number = int(input("Enter a number: "))
    # if number is 0 then stop reading ??
    if new_number == 0:
        reading = False
    else:
        numbers.append(new_number)

for number in numbers:
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")

# Activity 7
print("ACTIVITY 7")
a = input("What type of cover does the book have?").lower()
b = input("Is the book perfect-bound?").lower()

if a == "soft":
    if b == 'yes':
        print("Soft cover, perfect bound books are very popular!")


# Activity 8
print("ACTIVITY 8")
answer_8 = input("Where should I look?")
if answer_8 == 'bedroom':
    if input("Where in the bedroom should I look?").lower() == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif answer_8 == "in the bathroom":
    if input("Where in the bathroom should I look?") == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif answer_8 == "in the lab":
    if input("Where in the lab should I look?") == "on the table":
        print( "Yes! I found my battery!")
else:
    print("Found some tools but no battery.")


# Activity 9
print('ACTIVITY 9')
choice = input("Enter a type of adventure: scary/short OR safe/long ")
if choice == "scary" or choice == "short":
    print("Entering the dark forest!")
elif choice == "safe" or choice == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

# Activity 10
print('ACTIVITY 10')
hear = input("What did I hear ?: ")
see = input("What did I see ?: ")
if hear == "grrr" and see == "two red eyes":
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")


# Activity 11
print("ACTIVITY 11")
user_input = input("Do you like dogs or cats more ?: ").lower()
if user_input == 'dogs' or user_input == 'cats':
    if int(input(f"How many {user_input} do you have ?: ")) > 2:
        print(f"Wow! That's a lot of {user_input}.")






