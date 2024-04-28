"""
Napisz program w pythonie, który zrobi łańcuch decoratorów, i udekoruje podany text tak jak w przypadku html na BOLD, ITALIC, UNDERLINE

Input :

Hello world

Output:

<b><i><u>hello world</u></i></b>

"""


def add_bolt(func):
    def inner(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return inner


def add_italic(func):
    def inner(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return inner


def add_underline(func):
    def inner(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return inner


@add_underline
@add_italic
@add_bolt
def hello(text: str):
    return text


print(hello("Hello"))


def my_decorator(func):
    def inner(*args, **kwargs):
        print("decorator")
        return func(*args, **kwargs)

    return inner

@my_decorator
def my_func():
   print("Hello World")


my_func()