# Lists
# Task 1
def direction():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")

    return directions

def run():
    print(direction())

run()

# Task 2
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1 ]
    return path

def run():
    print("Moving...")
    new_list = movements()
    for i in range(0,len(new_list),2):
        print(f"{new_list[i]} for {new_list[i+1]} steps")

run()

# Task 3
def direction():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")
    return directions


def menu():
    print("Please select a direction: ")
    direction_list = direction()
    for i in range(len(direction_list)):
        print(f"{i}: {direction_list[i]}")

def run():
    menu()

run()


# Task 4
def direction():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction: ")
    new_direction_list = direction()
    for i in range(len(new_direction_list)):
        print(f"{i}: {new_direction_list[i]}")

    response = int(input())

    for _ in new_direction_list:
        return new_direction_list[response]





def run():
    route = []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu())

    print(route)
        # print(f"Escape route: {route}")

run()

# Tuples
# task 1
def likelihood():
    likelihoods = (50, 38, 27, 99, 4 )
    return min(likelihoods)

def run():
    min_val = likelihood()
    print(f"Minimum likelihood of falling: {min_val}%.")


run()

# task 2
def likelihood():
    likelihoods = (50, 38, 27, 99, 4 )
    return min(likelihoods), max(likelihoods)


def run():
    print(f"Minimum likelihood of falling: {likelihood()[0]}%\nMaximum likelihood of falling: {likelihood()[1]}%.")

run()

# task 3
def steps():
    return [("step 1", 50) , ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]

def run():
    list_of_tuples = steps()
    bad_steps = []
    good_steps = []
    for tup in list_of_tuples:
        if tup[1] >= 50:
            bad_steps.append(tup)
        else:
            good_steps.append(tup)
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()




