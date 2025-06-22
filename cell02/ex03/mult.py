#!/usr/bin/env python3
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
   
    product = num1 * num2
   
    if product > 0:
        result_description = "positive"
    elif product < 0:
        result_description = "negative"
    else: 
        result_description = "positive and negative" 
   
    print(f"The result is {result_description}.")
   
    print(f"{num1} * {num2} = {product}")
if __name__ == "__main__":
    main()
