"""

There was a test in your class and you passed it. Congratulations!But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return `True` if you're better, else `False`!

### **Note:**

Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
"""


def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


assert better_than_average([2, 3], 5)
assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)
assert better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)
assert not better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)
assert not better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21)