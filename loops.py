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