# Integer
int_var = 10
# Basic arithmetic operations
int_sum = int_var + 5
int_product = int_var * 2
int_division = int_var // 3
print(f"Integer Operations:\nSum: {int_sum}, Product: {int_product}, Division (Floor): {int_division}")

# Float
float_var = 10.5
# Basic arithmetic operations
float_sum = float_var + 5.5
float_product = float_var * 2
float_division = float_var / 3
print(f"\nFloat Operations:\nSum: {float_sum}, Product: {float_product}, Division: {float_division}")

# Stringi
string_var = "Hello"
# String concatenation
greeting = string_var + " World"
print(f"\nString Operations:\nConcatenation: {greeting}")

# List
list_var = [1, 2, 3, 4]
# List manipulation: appending and indexing
list_var.append(5)
first_element = list_var[0]
last_element = list_var[-1]
print(f"\nList Operations:\nList after appending: {list_var}, First element: {first_element}, Last element: {last_element}")

# Tuple
tuple_var = (1, "apple", 3.14)
# Tuple packing and unpacking
a, b, c = tuple_var
print(f"\nTuple Operations:\nPacked tuple: {tuple_var}, Unpacked values: {a}, {b}, {c}")

# Dictionary
dict_var = {"name": "Alice", "age": 25}
# Dictionary manipulation: Adding a new key-value pair and accessing value
dict_var["city"] = "New York"
name = dict_var["name"]
print(f"\nDictionary Operations:\nDictionary after adding a key-value pair: {dict_var}, Name: {name}")

# Set
set_var = {1, 2, 3, 4}
# Set operations: adding and removing elements, union
set_var.add(5)
set_var.remove(2)
another_set = {3, 4, 5, 6}
union_set = set_var.union(another_set)
print(f"\nSet Operations:\nSet after adding/removing elements: {set_var}, Union of sets: {union_set}")

# Boolean
bool_var = True
# Boolean logic
bool_and = bool_var and False
bool_or = bool_var or False
print(f"\nBoolean Operations:\nAND operation: {bool_and}, OR operation: {bool_or}")
