def search(file_name):
    print("Searching...")
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            print(f"Looked in {line.strip()}")
        print("...Done!")

def run():
    search('locations.txt')

run()