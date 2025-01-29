#   1. Loop Through a List
# Task: Iterate through a list and perform calculations.

# Instructions:
# Create a list of numbers: [10, 20, 30, 40, 50].
# Loop through the list and print each number multiplied by 2.
# Print the sum of all numbers in the list.




thisset = [10, 20, 30, 40, 50]
for x in thisset:
    print(x * 2)






# 2. List Comprehension
# Task: Create a filtered list using list comprehension.

# Instructions:
# Given a list of numbers [5, 12, 17, 24, 35], create a new list containing only numbers greater than 15.
# Square all the numbers in the new list using list comprehension.
# Print both the filtered and squared lists.


import math
set = [5, 12, 17, 24, 35]
# newlist = [x for x in set if x > 15 ]
newl=[]
# print(newlist)
 
for i in set:
 newl.append(i*i)
 
# listg = [x for x in newlist x * x ]

print( newl)


# 3. The Syntax
# Task: Create and manipulate lists.

# Instructions:
# Create a list of strings: ["apple", "banana", "cherry", "date"].
# Add "orange" to the list using append().
# Insert "grape" at index 2 using insert().
# Remove "date" from the list.
#  Print the final list

thislist = ["apple", "banana", "cherry", "date"]
thislist.append("orange")
 
thislist[2:2] = ["grape"]

thislist.remove("date")
print(thislist) 





# 4. Sort Lists
# Task: Sort numbers in a list.

# Instructions:
# Given a list of numbers [42, 12, 89, 33, 7], sort it in ascending order and print the result.
# Sort the same list in descending order and print the result.
# Use the reverse() method to reverse the list again.

thislist = [42, 12, 89, 33, 7]
thislist.sort(reverse = False)
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist.reverse()
print(thislist)


# 5. Sort List Alphanumerically
# Task: Sort a list of strings.

# Instructions:
# Create a list of names: ["Emma", "Olivia", "Liam", "Noah", "Sophia"].
# Sort the list alphabetically and print it.
# Sort the list in reverse alphabetical order and print it.
# Add "James" to the list, then sort again.

thislist = ["Emma", "Olivia", "Liam", "Noah", "Sophia"]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist) 
thislist.sort(reverse = False)
print(thislist) 

thislist.append("James")
print(thislist)