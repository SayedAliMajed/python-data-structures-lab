# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  rose_names = ["Peace", "Mister Lincoln", "Double Delight"]
  for element in rose_names:
      print(element)

# Call the function and print each element
example_list_function()
print("-----------------------------------------------------------")
# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ["Ahmed", "Sayed", "Khalil"]
    first_student= students[1]
    last_student = students[2]
    return first_student, last_student


# Call the function and print the result
print('Exercise 1:', manage_students())

print("-----------------------------------------------------------")
# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    students = ["Ahmed", "Sayed", "Khalil"]
    foods = ('Pizza', 'Burger', 'Baryani')
    meal = ""

    for food in foods:
        meal += food + " "
    
    return meal



# Call the function and print the result
print('Exercise 2:', combine_foods())

print("-----------------------------------------------------------")