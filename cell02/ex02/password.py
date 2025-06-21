#!/usr/bin/env python3
def main():
    # Store the correct password in a variable
    correct_password = "Python is awesome"
    #Prompt the user to enter a password
    entered_password = input("Enter the password: ")

    # Check if the entered password matches the correct one 
    if entered_password == correct_password: 
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
if __name__ == "__main__":
    main()
    
 