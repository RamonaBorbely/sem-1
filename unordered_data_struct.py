# Task 1
def observed():
    observations = {"Flying car", "Sky Scraper", "Laser", "Dome"}
    return observations

def run():
    print(observed())

run()

# Task 2
USER_INPUT_LEN = 7
def observed():
    observations = []
    for i in range(USER_INPUT_LEN):
        user_input = input("Please enter an observation: ")
        observations.append(user_input)
    return observations

def run():
    the_set = set()
    print("Counting observations...")
    new_list = observed()
    print(new_list)
    for i in range(len(new_list)):
        count_item = new_list.count(new_list[i])
        the_set.add((new_list[i], count_item))
    for s in the_set:
        print(f"{s[0]} observed {s[1]} times.")

run()

# Task 3
def observed():
    observations = []
    for i in range(5):
        new_item = input(f"Enter val {i + 1}: ")
        observations.append(new_item)
    return observations


def remove_observations(obs_list):
    while input("Do you want to remove observations ?: y / n ") == "y":
        val_to_remove = input("Which to remove: ")
        obs_list.remove(val_to_remove)
        if input("Do you want to remove observations ?: y / n ") == "n":
            break


def run():
    new_list = observed()
    remove_observations(new_list)
    print(new_list)
    new_set = set()
    for item in new_list:
        item_count = new_list.count(item)
        new_set.add((item, item_count))

    sorted_set = sorted(new_set)
    for item in sorted_set:
        print(f"{item[0]} observed {item[1]} times.")

run()

# dict
# task 4
def patern():
    sequences = {
        "Short Sequence": 3,
        "Medium Sequence": 2,
        "Long Sequence": 1
    }
    return  sequences

def run():
    print(patern())

run()

# task 5
def short_pattern():
    pattern = {
        "sequence": "101",
        "occurrences": 5
    }
    return  pattern

def mediun_pattern():
    pattern = {
        "sequence": "111000",
        "occurrences": 25
    }
    return pattern

def long_pattern():
    pattern = {
        "sequence": "1100110011001100",
        "occurences": 50
    }
    return pattern

def run():
    print("Analysing patterns...")
    new_dict = {
        "short sequence": short_pattern(),
        "medium sequence": mediun_pattern(),
        "long sequence": long_pattern()
    }
    for key, value in new_dict.items():
        print(key, value)
run()

