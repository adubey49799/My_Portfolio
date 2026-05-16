# %% [markdown]
# # Lab 2: Python Basics – Working with Collections and Functions
# 
# This notebook completes the required lab tasks for:
# 
# - Part 1: Tuples
# - Part 2: Lists
# - Part 3: Sets
# - Part 4: Functions
# 
# The goal of this lab is to practice Python collections and basic function creation using clear examples and comments.

# %% [markdown]
# ## Part 1: Tuples
# 
# In this section, we will practice creating, accessing, modifying through a workaround, unpacking, converting, finding duplicates, and reversing tuples.

# %%
# ============================================================
# Part 1: Tuples
# ============================================================

# 1. Create and Access
# A tuple is an ordered collection that cannot be changed after creation.
# Here, we create a tuple with at least 5 numerical values.
numbers_tuple = (10, 20, 30, 40, 50)

# Python uses zero-based indexing.
# The third item is at index 2.
print("1. Create and Access")
print("Tuple:", numbers_tuple)
print("Third item:", numbers_tuple[2])


# 2. Tuple Modification Workaround
# Tuples are immutable, so we cannot directly remove an item.
# Workaround:
# Step 1: Convert the tuple into a list.
# Step 2: Remove the item from the list.
# Step 3: Convert the list back into a tuple.
print("\n2. Tuple Modification Workaround")

original_tuple = (5, 10, 15, 20, 25)
temporary_list = list(original_tuple)

# Remove the value 15 from the list.
temporary_list.remove(15)

# Convert the modified list back into a tuple.
modified_tuple = tuple(temporary_list)

print("Original tuple:", original_tuple)
print("Tuple after removing 15:", modified_tuple)


# 3. Tuple Unpacking
# Tuple unpacking means assigning tuple values to separate variables.
print("\n3. Tuple Unpacking")

student_info = ("Alok", 35, "Data Science")
name, age, major = student_info

print("Name:", name)
print("Age:", age)
print("Major:", major)


# 4. Tuple to String
# A tuple of characters can be converted into a string using join().
print("\n4. Tuple to String")

characters_tuple = ("P", "y", "t", "h", "o", "n")
word = "".join(characters_tuple)

print("Characters tuple:", characters_tuple)
print("String:", word)


# 5. Find Duplicates
# We use one set to track values already seen.
# We use another set to store duplicate values.
print("\n5. Find Duplicates")

repeated_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 1, 7)

seen = set()
duplicates = set()

for item in repeated_tuple:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Tuple with repeated elements:", repeated_tuple)
print("Duplicate values:", duplicates)


# 6. Reverse Tuple
# Slicing with [::-1] reverses the tuple.
print("\n6. Reverse Tuple")

reverse_example_tuple = (100, 200, 300, 400, 500)
reversed_tuple = reverse_example_tuple[::-1]

print("Original tuple:", reverse_example_tuple)
print("Reversed tuple:", reversed_tuple)

# %% [markdown]
# ## Part 2: Lists
# 
# In this section, we will practice summing list values, removing duplicates, cloning lists, combining lists, sorting tuples inside a list, and using list slicing.

# %%
# ============================================================
# Part 2: Lists
# ============================================================

# 7. Sum of List
# The sum() function adds all numerical values in a list.
numbers_list = [12, 8, 15, 20, 5]
total_sum = sum(numbers_list)

print("7. Sum of List")
print("List:", numbers_list)
print("Sum of list:", total_sum)


# 8. Remove Duplicates
# This removes duplicate values while keeping the original order.
print("\n8. Remove Duplicates")

list_with_duplicates = [4, 2, 5, 2, 3, 4, 1, 5, 6]
unique_list = []

for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", list_with_duplicates)
print("List after removing duplicates:", unique_list)


# 9. Clone a List
# Below are three different ways to copy a list.
print("\n9. Clone a List")

original_list = [10, 20, 30, 40, 50]

# Method 1: Copy using slicing.
copy_method_1 = original_list[:]

# Method 2: Copy using the list() constructor.
copy_method_2 = list(original_list)

# Method 3: Copy using the copy() method.
copy_method_3 = original_list.copy()

print("Original list:", original_list)
print("Copy using slicing:", copy_method_1)
print("Copy using list():", copy_method_2)
print("Copy using copy():", copy_method_3)


# 10. Combine Lists
# The extend() method appends all items from one list to another list.
print("\n10. Combine Lists")

first_list = ["apple", "banana", "cherry"]
second_list = ["orange", "grape", "mango"]

first_list.extend(second_list)

print("Combined list:", first_list)


# 11. Sort by Last Element in Tuple
# The sorted() function sorts the list.
# The lambda function tells Python to sort using the last element of each tuple.
print("\n11. Sort by Last Element in Tuple")

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuple_list = sorted(tuple_list, key=lambda x: x[-1])

print("Original list of tuples:", tuple_list)
print("Sorted list by last element:", sorted_tuple_list)


# 12. List Slicing
# Slicing [:4] returns the first four items from the list.
print("\n12. List Slicing")

people_names = [
    "Alok", "John", "Maria", "Priya", "David",
    "Sophia", "Amit", "Linda", "Robert", "Nina"
]

first_four_names = people_names[:4]

print("All names:", people_names)
print("First 4 names:", first_four_names)

# %% [markdown]
# ## Part 3: Sets
# 
# In this section, we will practice creating sets, finding the intersection of two sets, and finding the union of two sets.

# %%
# ============================================================
# Part 3: Sets
# ============================================================

# 13. Create a Set
# A set is an unordered collection of unique values.
fruits_set = {"apple", "banana", "cherry", "orange", "mango"}

print("13. Create a Set")
print("Set of fruits:", fruits_set)


# 14. Set Intersection
# The intersection contains only values that are common to both sets.
print("\n14. Set Intersection")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

intersection_result = set_a.intersection(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Intersection:", intersection_result)


# 15. Set Union
# The union contains all unique values from both sets.
print("\n15. Set Union")

union_result = set_a.union(set_b)

print("Union:", union_result)

# %% [markdown]
# ## Part 4: Functions
# 
# In this section, we will practice creating functions to multiply list elements, calculate basic statistics, check range membership, and analyze dog running speeds.

# %%
# ============================================================
# Part 4: Functions
# ============================================================

# 16. Multiply List Elements
# This function takes a list of numbers and returns the product of all numbers.

def multiply_list_elements(numbers):
    """
    Return the product of all numbers in a list.
    """
    product = 1

    for number in numbers:
        product = product * number

    return product


numbers_to_multiply = [2, 3, 4, 5]
product_result = multiply_list_elements(numbers_to_multiply)

print("16. Multiply List Elements")
print("List:", numbers_to_multiply)
print("Product:", product_result)


# 17. Statistics Function
# This function returns the minimum, maximum, and average score.
print("\n17. Statistics Function")

test_scores = [88, 92, 75, 81, 95, 67, 89, 90]


def calculate_statistics(scores):
    """
    Return the minimum, maximum, and average score from a list.
    """
    minimum_score = min(scores)
    maximum_score = max(scores)
    average_score = sum(scores) / len(scores)

    return minimum_score, maximum_score, average_score


minimum, maximum, average = calculate_statistics(test_scores)

print("Test scores:", test_scores)
print("Minimum score:", minimum)
print("Maximum score:", maximum)
print("Average score:", round(average, 2))


# 18. Check Range Membership
# This function checks whether a number is inside a specified range.
print("\n18. Check Range Membership")


def is_number_in_range(number, start, end):
    """
    Check whether a number is within a specified range.
    This function includes both the start and end values.
    """
    return start <= number <= end


number_to_check = 15
range_start = 10
range_end = 20

if is_number_in_range(number_to_check, range_start, range_end):
    print(number_to_check, "is within the range", range_start, "to", range_end)
else:
    print(number_to_check, "is not within the range", range_start, "to", range_end)


# 19. Dog Speed Analyzer
# This nested list stores each dog breed and its maximum running speed.
print("\n19. Dog Speed Analyzer")

dog_speeds = [
    ["Greyhound", 45],
    ["German Shepherd", 30],
    ["Border Collie", 30],
    ["Poodle", 20],
    ["Bulldog", 15],
    ["Whippet", 35]
]


def analyze_dog_speeds(dogs):
    """
    Determine the fastest and slowest dog breeds based on max running speed.

    Each item in the dogs list contains:
    [dog breed, max speed]
    """
    fastest_dog = dogs[0]
    slowest_dog = dogs[0]

    for dog in dogs:
        if dog[1] > fastest_dog[1]:
            fastest_dog = dog

        if dog[1] < slowest_dog[1]:
            slowest_dog = dog

    return fastest_dog, slowest_dog


fastest, slowest = analyze_dog_speeds(dog_speeds)

print("Dog speeds:", dog_speeds)
print("Fastest dog breed:", fastest[0], "with speed", fastest[1], "mph")
print("Slowest dog breed:", slowest[0], "with speed", slowest[1], "mph")


