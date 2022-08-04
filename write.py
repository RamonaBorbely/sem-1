def search(file_name):
    print("Searching...", end="")
    sections = []
    books = []
    with open(file_name) as file:
        for line in file:
            if line.startswith("Section"):
                new_str = line.split(":")[1]
                sections.append(new_str.strip())
            else:
                books.append(line.strip())
        print("Done!")
    return sections, books


def save(file_name, data):
    print("Saving...", end="")
    with open(file_name, "w") as file:
        file.write(f"Sections: {data[0]}\n")
        file.write(f"Books: {data[1]}")
    print("Done!")


def run():
    data = search("books.txt")
    save("new_books.txt", data)


run()