#assignment 2 -- question1 check number is even or odd
number = int(input("enter a number: "))
if number %2 == 0:
    print(number, "is an even number")
else :
    print(number, "is an  odd number")

#question2 sum of integers from 1 to 50
sum = 0
for i in range(1,51):
    sum += i

print("Sum from 1 to 50 is:", sum)


