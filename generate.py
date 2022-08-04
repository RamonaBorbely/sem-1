import csv


def search(file_name):
    print("Searching...")
    data = {}
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Section"):
                section_name = line.split(":")[1].strip()
            else:
                data[section_name] = line.strip()
                if section_name not in data.values():
                    data[section_name] = line.strip()
                # missing one book ? this part still not helps

    print("Done!")
    return data


def run():
    data = search("books.txt")
    with open("generate_csv.csv", "w") as new_file:
        for key, value in data.items():
            new_file.write(f"{key}, {value}\n")

run()











