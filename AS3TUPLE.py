# Tuple Operations
# Create a tuple of numbers and:
# Find the maximum and minimum values.
# Calculate the sum of all elements.
# Count how many times a specific number appears.

thistuple = (10,20,11,12,1,3,22,67,)
print(min(thistuple))
print(max(thistuple))
print(sum(thistuple))


# Write a program that:
# Creates two sets of students enrolled in "Python" and "Data Science" courses.
# Finds the students who are enrolled in both courses (intersection).
# Lists students who are in either of the courses but not both (symmetric difference).

python = {"dev", "shailesh", "kalpu", "alpesh","riya","yash"}
datasci = {"manish", "yash","shiv", "riya","dev", "shailesh"}

python.intersection_update(datasci)
print(python) 
python.symmetric_difference_update(datasci)
print(python)




# Write a program that takes a list of integers with duplicates and returns a list with unique values, maintaining the original order.

set = {2,5,2,4,2,6,8,5,4,4,7,}
print(set)



# Set Methods
# Create a set of integers and:
# Add a new element to the set.
# Remove an existing element.
# Check if a specific element exists in the set.


set = {2,5,2,4,2,6,8,5,4,4,7,}
mylist = [100]
set.update(mylist)
print(set)


# # Basic Operations
# Create a dictionary with keys as country names and values as their capitals. Write a program that:
# Adds a new country-capital pair.
# Updates the capital of an existing country.
# Removes a country from the dictionary.


set = {"India","pakisthan","usa"}
mylist = ["nepal","uk"]

set.update(mylist)
print(set)
set.remove("uk")
print(set)