#!/usr/bin/env python3
def main():
    correct_password = "Python is awesome"
    entered_password = input("Enter the password: ")
    if entered_password == correct_password: 
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
if __name__ == "__main__":
    main()
    
 