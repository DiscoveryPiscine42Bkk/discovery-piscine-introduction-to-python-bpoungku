#!/usr/bin/env python3
def main():
    #Prompt for the first number
    num1 = float(input("Enter the first number: "))
    #Prompt foe the second number
    num2 = float(input("Enter the second number: "))
    #Calculate the product 
    product = num1 * num2
    #Determine the nature of the product 
    if product > 0:
        result_description = "positive"
    elif product < 0:
        result_description = "negative"
    else: 
        result_description = "positive and negative" #Special case for zero
    #Print the result description 
    print(f"The result is {result_description}.")
    #Print the actual multiplication result (FIXED: corrected format)
    print(f"{num1} * {num2} = {product}")
if __name__ == "__main__":
    main()
