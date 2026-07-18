# Functions_intro

# a = 3
# b = 8
# c = 9
# average = (a + b + c)/3
# print(average)

# a = 67
# b = 89 
# c = 78
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number"))
# b = int(input("Enter your number"))
# c = int(input("Enter your number"))
# average = (a + b + c)/3
# print(average)

# Function Definition

# def avg():
#     a = int(input("Enter your number"))
#     b = int(input("Enter your number"))
#     c = int(input("Enter your number"))

#     average = (a + b + c)/3
#     print(average)
    

# avg() # Function Call
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# avg()

# Quick_quiz
# def goodDay():
#     print("Good Day")

# goodDay()

# Function with arguments

# def goodday (name , ending):
#     print("Good Day, " + name )
#     print(ending)

# goodday ("Harry", "Thank you")
# goodday ("Rohan", "Thank you")
# goodday ("Divya", "Thanks")

# def goodday (name , ending):
#     print("Good Day, " + name )
#     print(ending)
#     return "done"

# a = goodday ("Harry", "Thank you")
# print(a)

# Default_argument

# def goodday(name, ending= "Thank you"):
#     print(f"Good Day, {name}")
#     print(ending)

# goodday("Harry", "Thanks")
# goodday("Rohan")

# Recursion
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1 
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial of (n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")