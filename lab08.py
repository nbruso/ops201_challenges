# Script Name:                  Ops Challenge 08          
# Author:                       Dominique Bruso
# Date of latest revision:      12/06/2023
# Purpose:                      To practice python
# Execution:                    python lab08.py
# Source:                       https://chat.openai.com/share/bb5eb39c-3595-4437-999e-f8b0057ead04

import time

# Assign to a variable a list of ten fruit elements.
my_list = ["apple", "banana", "cherry", "date", "berry", "fig", "grape", "melon", "kiwi", "lemon"]

# Part 1: List Operations
print("PART 1: LIST OPERATIONS")
print("Original List:", my_list)
time.sleep(2)

# Print the fourth element of the list.
print("\nFourth Element:", my_list[3])
time.sleep(2)

# Print the sixth through tenth element of the list.
print("\nSixth through Tenth Elements:", my_list[5:10])
time.sleep(2)

# Change the value of the seventh element to “onion”.
my_list[6] = "onion"
print("\nModified List:", my_list)
time.sleep(2)

# Part 2: List Methods
print("PART 2: LIST METHODS")
# Use Python methods to manipulate the elements in the list.

# append(): Add a new fruit to the end of the list.
my_list.append("mango")
print("\nAfter Append:", my_list)
time.sleep(2)

# clear(): Remove all elements from the list.
my_list.clear()
print("\nAfter Clear:", my_list)
time.sleep(2)

# Reassigning the list for further operations
my_list = ["apple", "banana", "cherry", "date", "berry", "fig", "grape", "melon", "kiwi", "lemon"]

# copy(): Create a shallow copy of the list.
copied_list = my_list.copy()
print("\nCopied List:", copied_list)
time.sleep(2)

# count(): Count the occurrences of a specific fruit in the list.
count_of_banana = my_list.count("banana")
print("\nCount of 'banana':", count_of_banana)
time.sleep(2)

# extend(): Extend the list by appending fruit from an iterable.
extension = ["orange", "peach"]
my_list.extend(extension)
print("\nAfter Extend:", my_list)
time.sleep(2)

# index(): Find the index of a specific fruit in the list.
index_of_date = my_list.index("date")
print("\nIndex of 'date':", index_of_date)
time.sleep(2)

# insert(): Insert a new fruit at a specific index.
my_list.insert(2, "blueberry")
print("\nAfter Insert:", my_list)
time.sleep(2)

# pop(): Remove and return the fruit at a specific index (default is the last fruit).
popped_element = my_list.pop(4)
print("\nPopped Element:", popped_element)
print("\nAfter Pop:", my_list)
time.sleep(2)

# remove(): Remove the first occurrence of a specific fruit from the list.
my_list.remove("grape")
print("\nAfter Remove:", my_list)
time.sleep(2)

# reverse(): Reverse the order of fruit in the list.
my_list.reverse()
print("\nAfter Reverse:", my_list)
time.sleep(2)

# sort(): Sort the fruit in ascending order.
my_list.sort()
print("\nAfter Sort:", my_list)
time.sleep(2)

# Part 3: Tuple, Set, and Dictionary
print("PART 3: TUPLE, SET, AND DICTIONARY")
# Create one tuple.
my_tuple = ("apple", "banana", "cherry", "date", "berry")
print("\nTuple:", my_tuple)
time.sleep(2)

# Create one set.
my_set = {"apple", "banana", "cherry", "date", "berry"}
print("\nSet:", my_set)
time.sleep(2)

# Create one dictionary with fruit-related information.
fruit_dict = {
    "fruit_name": "Apple",
    "color": "Red",
    "taste": "Sweet",
    "quantity": 5
}
print("\nFruit Dictionary:", fruit_dict)
time.sleep(2)











