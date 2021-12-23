prompt = "\nTell me what topping you want on your pizza: "
prompt += "\nEnter 'quit' to stop adding toppings. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"Adding {message}!")

print("\nFinished making your pizza!")