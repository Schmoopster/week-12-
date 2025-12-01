# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
temperature = int(input("What is today's temperature?"))
if 80 <= temperature <110:
    print("It is hot outside")
elif 70 <= temperature < 80:
    print("It is warm outside")
elif 40 <= temperature <70:
    print("It is cool outside")
elif -10 <= temperature <40:
    print("It is cold outside")
else:
    print("Extreme temperature warning!")