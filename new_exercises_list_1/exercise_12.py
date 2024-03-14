DEFAULT_FAVORITE_NUMBER = 1


def not_a_great_function(name, age, *, favorite_color, favorite_numbers=[]):
    if not favorite_numbers:
        favorite_numbers.append(DEFAULT_FAVORITE_NUMBER)

    return User(
        name=name,
        age=age,
        favorite_numbers=favorite_numbers,
        favorite_color=favorite_color
    )

"cannot add favorite color, nave no default value"
