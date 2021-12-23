prompt = "\nHow old are you? (Any non-number response will end the program.) "

active = True

while active:
    age = input(prompt)
    if age.isdigit():
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15
    else:
        active = False
    
    if active:
        print(f"\nYour ticket costs ${price}.")

print("\nEnjoy the movie!")