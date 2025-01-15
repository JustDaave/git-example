import random

print("Hi! I'm going to try to guess your age.")
name = input("What is your name? ")

guessed = False
low = 15
high = 30

while not guessed:
    guess = random.randint(low, high)
    user_response = input(f"Are you {guess} years old? (y/n): ").strip().lower()
    
    if user_response == 'y':
        print(f"Haha! {name} is {guess} years old.")
        guessed = True
    else:
        hint = input(f"Is your age higher or lower than {guess}? (higher/lower): ").strip().lower()
        if hint == "higher":
            low = guess + 1
        elif hint == "lower":
            high = guess - 1
        else:
            print("Please answer with 'higher' or 'lower'.")
        
        if low > high:
            print(f"Something doesn't add up, {name}. Are you sure about your hints?")
            break
  
