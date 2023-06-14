import ai_gen_match
import time
from pydantic import BaseModel

"""
1. Concise syntax:
Thought to test the speed difference between a match case and a dict lut.
"""
test_params = (0, 1, 5)

lut = {
    0: "Zero",
    1: "One",
    None: "Other"
}

print("="*50)
for i in test_params:
    case1 = time.perf_counter()
    print(f"case1: {ai_gen_match.check_value(i)}")
    runtime1 = time.perf_counter() - case1
    print(f"case1: {runtime1}")
    
    case2 = time.perf_counter()
    res = None
    try:
        res = res or lut[i]
    except KeyError:
        res = lut[None]
    runtime2 = time.perf_counter() - case2
    print(f"case2: {res}")
    print(f"case2: {runtime2}")

    if runtime1 < runtime2:
        print("match was the winner")
    else:
        print("dict lut won")
    print("="*50)

# My conclusion: It seems that the LUT may be faster, but the match case is better
# for handling default values.
# LUTs are maybe for the times you know all your options?




"""
5. Simplified control flow: 
The check_number() function showcases simplified control flow by handling different cases based on the value being checked.
"""

# Had ChatGPT generate this as well:
class InputData(BaseModel):
    data: int

def check_number(value: InputData) -> str:
    # Not sure if Pydantic would be a better option? 
    # Seems like it would not. Got: TypeError: '<' not supported between instances of 'InputData' and 'int'
    if not isinstance(value, int):  
        return "Other"
    
    match value:
        case 0:
            return "Zero"
        case n if n < 0:
            return "Negative"
        case n if n > 0:
            return "Positive"
        case _:
            return "Other"


print(check_number(InputData(data=0)))  # Output: Zero
print(check_number(-5))  # Output: Negative
print(check_number(10))  # Output: Positive
print(check_number(InputData(data=0.5)))  # Output: Other   <-- This returns a 'Positive', as it should I guess. Need input validation and make sure it is an int.
