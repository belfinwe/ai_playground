from typing import Union, List, Tuple

"""
Doc strings are what ChatGPT had to say about each function.
Promt: Based on the numbered list you gave above, could you please generate an extensive example of each point? Please use Python3.10.
"""


# 1. Concise syntax
"""
Concise syntax: 
The check_value() function uses the match statement to check different values and return corresponding strings in a concise manner.
"""
def check_value(value: int) -> str:
    match value:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case _:
            return "Other"


print(check_value(0))  # Output: Zero
print(check_value(1))  # Output: One
print(check_value(5))  # Output: Other


# 2. Structural pattern matching
"""
Structural pattern matching: 
The process_data() function utilizes the match statement to process different types of data (a list or a tuple) and perform different actions based on their structure.
"""
def process_data(data: Union[List[int], Tuple[int, str]]) -> str:
    match data:
        case [x, y]:
            return f"List: {x}, {y}"
        case [int(x), int(y), int(z)]:                     # Added my own to test
            return f"List: {x}, {y}, {z}"
        case (x, y):
            return f"Tuple: {x}, {y}"
        case (int(x), int(y), int(z)):                     # Added my own to test
            return f"Tuple: {x}, {y}, {z}"
        case _:
            return "Invalid data"


print(process_data([1, "hello"]))  # Output: List: 1, hello
print(process_data((2, "world")))  # Output: Tuple: 2, world
print(process_data({"key": "value"}))  # Output: Invalid data

# My own tests
print(process_data((2, "world", "class")))  # Output: Invalid
print(process_data((2, 3, 4)))  # Output: List
print(process_data([2, 3, 4]))  # Output: List



# 3. Exhaustiveness checking
"""
Exhaustiveness checking: 
The process_age_group() function demonstrates exhaustiveness checking by handling specific age groups and raising a MatchError for unhandled cases.
"""
def process_age_group(age: int) -> str:
    match age:
        case 0:
            return "Infant"
        case 1 | 2 | 3:
            return "Toddler"
        case 4 | 5 | 6:
            return "Child"
        # Missing case for other ages


try:
    print(process_age_group(0))  # Output: Infant
    print(process_age_group(2))  # Output: Toddler
    print(process_age_group(5))  # Output: Child
    print(process_age_group(10))  # ~~Raises MatchError~~ Seems to be returning None
except Exception as err:  # Changed from `MatchError`.
    print(f"Age group not found: {err}")


# 4. Type checking integration
"""
Type checking integration: 
The process_input() function uses the match statement to differentiate between different data types and handle them accordingly.

def process_input(data: str) -> str:
    '''
    Must admit I don't know match well enough to know if this should work, or
    is better handled as just an if test or look up.
    '''
    match data:
        case str:
            return f"Input: {data}"
        case int:
            return "Invalid data type"


print(process_input("Hello"))  # Output: Input: Hello
print(process_input(42))  # Output: Invalid data type
"""

# 5. Simplified control flow
"""
Simplified control flow: 
The check_number() function showcases simplified control flow by handling different cases based on the value being checked.
"""
def check_number(value: int) -> str:
    match value:
        case 0:
            return "Zero"
        case n if n < 0:
            return "Negative"
        case n if n > 0:
            return "Positive"
        case _:
            return "Other"


print(check_number(0))  # Output: Zero
print(check_number(-5))  # Output: Negative
print(check_number(10))  # Output: Positive
print(check_number(0.5))  # Output: Other   <-- This returns a 'Positive', as it should I guess. Need input validation and make sure it is an int.


# 6. Extensibility
"""
Extensibility: 
The CustomPattern class demonstrates the extensibility of the match statement by defining a custom pattern and handling it separately.
"""
class CustomPattern:
    def __match_args__(self):
        return ("CustomPattern",)


def process_custom_pattern(data: CustomPattern) -> str:
    match data:
        case CustomPattern():
            return "Custom pattern matched"
        case _:
            return "Pattern not matched"


pattern = CustomPattern()
print(process_custom_pattern(pattern))  # Output: Custom pattern matched
print(process_custom_pattern("test"))  # Output: Pattern not matched
