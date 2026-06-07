# ================================================================
#         PYTHON HW : LIST · SET · TUPLE · DICT
   

# ================================================================
#                           LISTS
# ================================================================

# Problem L1: List Info
# ---------------------
# Use this list in your code:

nums = [10, 20, 30, 40, 50]
print("Count: " , len(nums))
print("Sum: " , sum(nums))
print("First: " , nums [0])
print("Last: " , nums [-1])

# Print:
#   - The number of items in the list.
#   - The sum of all items.
#   - The first item.
#   - The last item.

# Expected output:
#     Count: 5
#     Sum: 150
#     First: 10
#     Last: 50

print("-"*40)
# Problem L2: Add and Remove
# --------------------------
# Use this list:

shopping = ["bread", "milk", "eggs"]
shopping.append("cheese")
shopping.remove("milk")
print(shopping)

# Do these steps in order:
#   1. Add "cheese" to the end.
#   2. Remove "milk" from the list.
#   3. Print the final list.

# Expected output:
#     ['bread', 'eggs', 'cheese']

print("-"*40)

# ================================================================
#                            SETS
# ================================================================

# Problem S1: Create and Add
# --------------------------
# Use this set:

colors = {"red", "blue", "green"}
colors.add("yellow")
colors.add("red")
print("Size: ", len(shopping))
print("red in set: ", "red" in colors)
print("yellow in set: ", "yellow" in colors)
# Do these steps:
#   1. Add "yellow" to the set.
#   2. Try to add "red" again (it's already there — see what happens).
#   3. Print the size of the set.
#   4. Check if "red" and "yellow" are in the set, print True/False.

# Expected output:
#     Size: 4
#     red in set: True
#     yellow in set: True

print("-"*40)

# Problem S2: Remove Duplicates from a List
# -----------------------------------------
# Use this list:

nums = [1, 2, 2, 3, 4, 4, 5, 1]
nums = set(nums)
print("Unique values" , nums)
print("Count of unique values: " , len(nums))

# Convert it to a set to remove duplicates, then print:
#   - The set.
#   - The size of the set.

# Expected output:
#     Unique values: {1, 2, 3, 4, 5}
#     Count of unique values: 5

# (Set display order may vary — that's normal for sets.)

print("-"*40)

# Problem S3: Set Operations
# --------------------------
# Use these two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union: ", a | b)
print("Intersection: " , a & b)
print("In a but not in b: " , set.intersection(a - b))

# Print:
#   - Their union.
#   - Their intersection.
#   - Items in `a` but NOT in `b`.

# Expected output:
#     Union: {1, 2, 3, 4, 5, 6}
#     Intersection: {3, 4}
#     In a but not in b: {1, 2}
print("-"*40)

# ================================================================
#                           TUPLES
# ================================================================

# Problem T1: Create and Access
# -----------------------------
# Create a tuple representing a person:

person = ("Sara", 25, "Riyadh")
print("Name: ", person[0])
print("Age: ", person[1])
print("City: ", person[2])

# Print:
#   - The name (first item).
#   - The age (second item).
#   - The city (third item).

# Expected output:
#     Name: Sara
#     Age: 25
#     City: Riyadh

print("-"*40)

# Problem T2: Immutability Check
# ------------------------------
# Use this tuple:

colors = ("red", "green", "blue")

# Try to do this:

#colors[0] = "yellow"
print("Length" , len(colors))
print("red in tuple: " , "red" in colors)


# Then print:
#   - The length of the tuple.
#   - Whether "red" is in the tuple (True/False).

# Expected output:
#     Length: 3
#     red in tuple: True
print("-"*40)

# ================================================================
#                            DICTS
# ================================================================

# Problem D1: Create and Access
# -----------------------------
# Create a dict representing a student:

student = {"name": "Ali", "age": 17, "grade": "11"}
print("Name: ", student["name"] )
print("Age: ", student["age"] )
print("Grade: ", student["grade"] )

# Print:
#   - The student's name.
#   - The student's age.
#   - The student's grade.

# Expected output:
#     Name: Ali
#     Age: 17
#     Grade: 11

print("-"*40)

# Problem D2: Add and Update
# --------------------------
# Use this dict of prices:

prices = {"apple": 3, "banana": 2}
prices["mango"] = 5
prices["apple"] = 4

print(prices)

print("-"*40)
# Do these steps:
#   1. Add a new item "mango" with price 5.
#   2. Update the price of "apple" to 4.
#   3. Print the final dict.

# Expected output:
#     {'apple': 4, 'banana': 2, 'mango': 5}


# Problem D3: Keys and Membership
# -------------------------------
# Use this dict:

user = {"name": "Sara", "email": "sara@example.com", "city": "Jeddah"}
print("Keys: " , list(user.keys()))
print("'name' in dict: ", 'name' in user)
print("'phone' in dict: ", 'name' in user)

# Print:
#   - All the keys (as a list).
#   - Whether "name" is a key in the dict (True/False).
#   - Whether "phone" is a key in the dict (True/False).

# Expected output:
#     Keys: ['name', 'email', 'city']
#     'name' in dict: True
#     'phone' in dict: False