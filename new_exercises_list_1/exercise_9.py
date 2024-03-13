from typing import Optional, List


def find_first_odd_number(numbers: Optional[List[int]]) -> Optional[int]:
    if not numbers:
        return None

    return next((x for x in numbers if x % 2), None)

"""best is to declarate numbers as optional list of integers, and returns optional integer value"""

print(find_first_odd_number([1, 3]))
print(find_first_odd_number([4, 3]))
print(find_first_odd_number([5, 3]))
print(find_first_odd_number([7, 3]))