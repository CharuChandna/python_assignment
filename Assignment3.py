#question 1 

def factorial(number):
    if number == 0 or number == 1:
        return 1 
    else:
        return number * factorial(number - 1)

# Get input from user
num = int(input("Enter a number to calculate its factorial: "))

# Check for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("The factorial of", num, "is:", factorial(num))


#-----------------------
import math

# Step 1: Ask the user for input
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
if num > 0:
    square_root = math.sqrt(num)
    natural_log = math.log(num)
else:
    square_root = "Not defined for negative numbers"
    natural_log = "Not defined for zero or negative numbers"

sine_value = math.sin(num)  # Sine function works for all real numbers (in radians)

# Step 3: Display the results
print("\n--- Results ---")
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm (ln) of {num} is: {natural_log}")
print(f"Sine of {num} (in radians) is: {sine_value}")
