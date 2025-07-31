# Factorial Number 

def factorial_number(num):
    if num < 0:
        print(f"Provide correct input to code {num}")
    elif num == 0 or num == 1:
        print(f"The factorial of {num} is 1")
    else:
        result = 1
        for i in range(1,num+1):
            result *= i
        print(f"The given Number {num} factioral is {result}")

user_input = int(input("Enter the number you wan't to factorial : "))
factorial_number(user_input)
