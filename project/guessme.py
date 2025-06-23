from random import randint
print("Welcome to the Guess the Number game!")
print("I've generated a secret number between 1 and 100. You have 5 guesses.")

my_number = randint(1,100)
low = 1
high = 100

for try_num in [1, 2, 3, 4, 5]: 
    guess = input("Enter your guess:")
    if not guess.isdigit():
        print("Please enter a number!")
        continue
    guess = int(guess)

    if guess < low or guess > high: 
        print(f"Please guess between {low} and {high}!")
        continue

    if guess == my_number:
        print("Wow you're correct!")
        break
    elif guess < my_number:
        low = guess + 1
        print(f"The secret number is between {low} and {high}.")        
    else:
        high = guess - 1
        print(f"The secret number is between {low} and {high}.")   

    print(f"Attempts left: {5 - try_num}\n")     
else:
    print(f"GAME OVER! MY NUMBER WAS {my_number} ") 
