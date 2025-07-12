#question 1 
try:
    with open('sample1.txt', 'r') as file:
        print("File content:")
        for line in file:
            print(line.strip())  # Use .strip() to remove extra newlines
except FileNotFoundError:
    print("Error: The file 'sample1.txt' was not found.")



#question2 

user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("data sucessfully written to the output.txt.")

additional_data = input("Enter additional data to append to the file: ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("data sucessfully appended")

print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
