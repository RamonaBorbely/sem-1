# Activity 1
print("ACTIVITY 1")
user_answer = int(input("How many cables should I remove ?: "))
removed_cables = 0
while removed_cables < user_answer:
    print(f"Removing calbe {removed_cables +1}")
    removed_cables += 1


# Activity 2
print("ACTIVITY 2")
answer = int(input("How many live cables must I avoid ?: "))

cables = 0
while cables < answer:
    print("Avoiding...", end=" ")
    print(f"Done! {cables + 1} live cable avoided!")
    cables += 1

print("All live cables have been avoided.")


# Activity 3
print("ACTIVITY 3")
bars = int(input("How many bars should be charged ?: "))
bares_charged = 0
emo = "🔷"

while bares_charged <= bars:
    print(emo * bares_charged)
    print(" ")
    bares_charged += 1

print("The battery is fully charged.")


# Activity 4
print("ACTIVITY 4")
phrase = input("Please enter a phrase: ")

i = 0
while i < len(phrase):
    print("Bop", end=" ")
    i += 1


# Activity 5
print("\nACTIVITY 5")
print("Calculating the sum of the first 100 numbers...")

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"...Done! The answer is {sum}.")


# # Activity 6
# print("ACTIVITY 6")
num_to_add = int(input("How many numbers should I sum up ?:"))
count = 0
sum = 0

while count < num_to_add:
    num = int(input(f"Please enter number {count +1} of {num_to_add}: \n"))
    sum += num
    count +=1

print(f"The answer is {sum}")


# Activity 7
print("ACTIVITY 7")
n = int(input("Please enter a number: "))

factorial = 1
j = 1
while j <= n:
    factorial *= j
    j += 1

print(f"The factorial is {factorial}.")


# Activity 8
print("ACTIVITY 8")
num_of_mountains = int(input("How many mountains should I display ?: "))

print("Displaying...")
for i in range(num_of_mountains):
    print("""    __
          /  \_
         /^    \,
        /  ^    \_
      _/ ^ ^     ^\,
     /  ^     ^    \
     """)

print("Done!")


# Activity 9
print("ACTIVITY 9")
steps = int(input("How far are we from the cave ?: "))
for i in range(steps, 0, -1):
    print(f"{i} steps remaining")

print("\nWe have reached the cave!")

# Activity 10
print("ACTIVITY 10")
brightness = int(input("What level of brightness is required ?: "))

for i in range(2, brightness+1, 2):
    print(f"\nBeep's brightness level: ", end="" '*' * i)
    print(f"\nBop's brightness level: ", end="" '*' * i)
    print(" ")
print("Adjustments complete!")


# Activity 11
print("ACTIVITY 11")
user_in = input("What strange markings do you see ?: \n ♯☼⌂╝ℓ ")

print("identifying...")
for i in range(len(user_in)):
    print(f"index i: {user_in[i]}")

print("\nDone!")


# Activity 12
print("ACTIVITY 12")
word_to_reverse = input("What phrase do you see ?: ")
reversed_word = ""

print("Reversing...")
for ch in range(len(word_to_reverse) -1, -1, -1):
    reversed_word += word_to_reverse[ch]

print(f"The phrase is: {reversed_word}")


# Activity 13
print("ACTIVITY 13")

user_phrase = input("What phrase do you see ?: ")
new_str = ''
for p in user_phrase:
    # will add current character to existing whole string that exist at that time of each loop
    new_str = p + new_str
print(f"The phrase is: {new_str}")

# this will aslo reverse a string
a_string = "hello everybody"
print(a_string[::-1])

# Some string slice
name = "Ramona"
print(f"First 3 ch: {name[:3]}")
print(f"Last 3 ch: {name[3:]}")
print(f"Last ch: {name[-1]}")
print(f"First ch: {name[0]}")
print(f"Reversed: {name[::-1]}")


# Activity 14
print("ACTIVITY 14")

rows = int(input("How many rows should I have ?: "))
columns = int(input("How many columns should I have ?: "))
symb = ":)"

for row in range(rows):
    for column in range(columns):
        print(symb, end="")
    print(" ")


# Activity 15
print("ACTIVITY 15")

marker = input("Marker: ")
seq = input("Sequence: ")

markers = []

for s in range(len(seq)):
    if seq[s] == marker:
        markers.append(s)


print(f"Distance: {markers[1] - markers[0] -1}")






