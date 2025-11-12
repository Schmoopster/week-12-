# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a == b)   # checks for equality # False
print(a != b)   # checks if it is not equal to another value# True
print(a > b)    # checks for greater than # False
print(a < b)    # checks for less than # True
print(a >= b)   # checks for greater than or equal to # False
print(a <= b)   # checks for less than or equal to # True


#predict the output of the following comparisons:
10 > 5 # Output: True
7 == 2 * 3 + 1 # Output: True
8 != 8 # Output: False
4 <= 2 + 2 # Output: True

# Write 3 examples that result in True and 3 that result in False.
print(4 > 8) #Output: False
print(3 * 2 + 4 - 1 == 9) # Output: True
print(4 <= 4) # Output: True
# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
# Asking student for score
score = int(input("What is your score?"))
#make this program for all grading spectrums
# If the score is between 90-100, you got an A
#if the score is between 80-89, you got a B
# If the score is between 70-80, you got a C
# If the score is between 60-69, you got a D
# else you failed
if score >= 60:
    print("You passed the test!")
else:
    print("You didn't pass the test.")
if score == 100:
    print("You aced the test, good job!")
if score >= 90:
    print("You got an A")
if score <= 89 & score >= 80:
    print("You got a B")
if score <= 79 &score  >= 70:
    print("You got a C")
if score <= 69 & score >= 60:
    print("You got a D")
if score <= 59:
    print("You failed, im not letting you graduate.")
# Ask for a password
    password = input("What is your password?")
