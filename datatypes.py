#  ASSIGNMENT_NO_01 

# -python data types and keywords;

# -python data types:
# Python comes with several built-in data types that you can use to store different kinds of information
# below down all the most commonly used data types.

# 1 - int: Whole numbers without a fractional part.

num_int:int = 10
print("number:", num_int)

# 2 - float: A number with a fractional part or numbers with decimals.

num_float:float = 10.5
print("float:", num_float)

# 3 - str: Text data.

text_data:str= "Hello World"
print("string:", text_data)

# 4 - bool: A boolean value that can be either True or False.

boolean_value:bool = True
print("boolean:", boolean_value)

# 5 - list: A collection of items which are ordered and mutable.

cities:list[str] = ["karachi", "lahore", "Islamabad"]
print("pakistan Cities:", cities)

# 6 - tuple: A collection of items which are ordered and immutable.

countries:tuple[str] = ("pakistan", "dubai", "South korea", "Saudi Arabia")
print("Countries:", countries)

# 7 - dict: A collection of key-value pairs which are unordered and mutable.

user_data:dict[str, str] = {"name": "khadija", "age": "20", "city": "Karachi"}
print("User Data:", user_data)

# 8 - set: A collection of unique items which are unordered and mutable.

numbers_set:set[int] = {5, 4, 3, 2, 1, 5} # Duplicates are removed automatically
print("Unique Numbers Set:", numbers_set)

# 9 - frozenset: Immutable version of set.
frozen_numbers_set:set[int] = frozenset({6, 7, 8, 9, 9})
print("Frozen Numbers Set:", frozen_numbers_set)

# 10 - None: A special type representing the absence of a value.

empty_value: None = None
print("Empty Value:", empty_value)
print(type(empty_value))

# 11 - range: understand range by example: It represents an immutable sequence of numbers, which is especially useful for iterating over a sequence in loops.

for i in range(1, 15):
    print(i)









