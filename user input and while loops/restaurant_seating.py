num_people = input("How many people are in your dinner group? ")
num_people = int(num_people)

if num_people > 8:
    print(f"You'll have to wait for a table.")
else:
    print(f"Your table is ready!")