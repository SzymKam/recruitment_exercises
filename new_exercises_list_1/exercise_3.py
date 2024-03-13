"""
Get a list of users from the list for users in the USA.
users = [
    {"name": "Bill", "age": 37, "country": "USA"},
    {"name": "Susan", "age": 21, "country": "Canada"},
    {"name": "Glenda", "age": 61, "country": "Britain"},
    {"name": "Astro", "age": 121, "country": "USA"},
]
"""

users = [
    {"name": "Bill", "age": 37, "country": "USA"},
    {"name": "Susan", "age": 21, "country": "Canada"},
    {"name": "Glenda", "age": 61, "country": "Britain"},
    {"name": "Astro", "age": 121, "country": "USA"},
]
# 1
usa_users = list()
for user in users:
    if user["country"] == "USA":
        usa_users.append(user)
print(usa_users)

# 2
result = [user for user in users if user["country"] == "USA"]
print(result)
