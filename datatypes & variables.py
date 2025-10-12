# Python - Data Types and Variables 

# -------------------------------
# Basic Data Types
# -------------------------------

# Integer
age = 25
print("Integer:", age, type(age))

# Float
pi = 3.14159
print("Float:", pi, type(pi))

# String
name = "Alice"
print("String:", name, type(name))

# Boolean
is_active = True
print("Boolean:", is_active, type(is_active))

# NoneType
nothing = None
print("NoneType:", nothing, type(nothing))

print("\n-------------------------------")
# -------------------------------
# Sequence Data Types
# -------------------------------

# List - ordered, mutable
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, type(fruits))

# Tuple - ordered, immutable
coordinates = (10.5, 20.3)
print("Tuple:", coordinates, type(coordinates))

# Range
numbers = range(5)
print("Range:", list(numbers), type(numbers))

# String - also a sequence
text = "hello"
print("String as sequence:", text, type(text))

print("\n-------------------------------")
# -------------------------------
# Set Types
# -------------------------------

# Set - unordered, unique elements
unique_numbers = {1, 2, 3, 2}
print("Set:", unique_numbers, type(unique_numbers))

# Frozenset - immutable set
frozen = frozenset([4, 5, 6])
print("Frozenset:", frozen, type(frozen))

print("\n-------------------------------")
# -------------------------------
# Mapping Type
# -------------------------------

# Dictionary - key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}
print("Dictionary:", person, type(person))

print("\n-------------------------------")
# -------------------------------
# Type Conversion
# -------------------------------

num_str = "100"
num_int = int(num_str)
print("Type Conversion str -> int:", num_int, type(num_int))

flt = float("3.5")
print("Type Conversion str -> float:", flt, type(flt))

s = str(123)
print("Type Conversion int -> str:", s, type(s))

char_list = list("abc")
print("Type Conversion str -> list:", char_list, type(char_list))

print("\n-------------------------------")
# -------------------------------
# Type Checking
# -------------------------------

print("Type of 'age':", type(age))
print("Type of 'fruits':", type(fruits))
print("Type of 'person':", type(person))

# End of Script
