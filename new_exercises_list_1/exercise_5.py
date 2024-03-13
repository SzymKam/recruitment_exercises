DEFAULT_SALUTATIONS = "Hello"


def enhanced_greeting(name: str, salutation: str = DEFAULT_SALUTATIONS):
    salutation = salutation.replace("!", "")
    return f"{salutation} {name}"


print(
    enhanced_greeting("Mr. Jones"),
    enhanced_greeting("Mrs. Jones", "Good Morning!"),
    enhanced_greeting("Mrs. Smith", "Good afternoon")

)
"""any of answers are not right"""
