from functools import partial
from typing import Iterable, Optional


def print_sum(num_list: Iterable[int], msg: Optional[str] = None):
    total = sum(num_list)
    print(f"{msg}: {total}" if msg else total)


calculate_total_cost = partial(print_sum, [11.22, 54.21, 100])
# its print_sum function with added interable num_list
calculate_total_cost([50, 60])
# now we call parial function of print_sum, and just add mgs arg


# partial function return basic function with added parameter
# we can call them, and this parameters given before are saved