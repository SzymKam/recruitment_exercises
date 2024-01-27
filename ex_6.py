"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""

def move_zeros(lst):
    # return [i for i in lst if i != 0] + [0] * str(lst).count('0')
    lst.sort(key=lambda v: v == 0)
    return lst


    # for element in lst:
    #     if element == 0:
    #         lst.remove(element)
    #         lst.append(element)
    #
    # return lst



assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ==  [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert move_zeros([]) == []
assert move_zeros([0, 0]) == [0,0]

