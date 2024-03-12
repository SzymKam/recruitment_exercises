"""
Write a function that will return all numbers that exist in both lists.
list_a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
list_b = [4, 8, 15, 16, 23, 42]
"""
# 1
list_a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
list_b = [4, 8, 15, 16, 23, 42]

result = set(list_a + list_b)
print(sorted(result))

# 2
for element in list_b:
    if element not in list_a:
        list_a.append(element)

print(sorted(list_a))
