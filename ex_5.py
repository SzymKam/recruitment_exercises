"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
"""


def digitize(n):
    # result = []
    # for element in str(n):
    #     result.append(int(element))
    # result = result[::-1]
    # return result
    return [int(num) for num in str(n)[::-1]]



assert digitize(35231) == [1, 3, 2, 5, 3]
assert digitize(0) == [0]
assert digitize(23582357) == [7,5,3,2,8,5,3,2]
assert digitize(984764738) == [8,3,7,4,6,7,4,8,9]
assert digitize(45762893920) == [0,2,9,3,9,8,2,6,7,5,4]
assert digitize(548702838394) == [4,9,3,8,3,8,2,0,7,8,4,5]

