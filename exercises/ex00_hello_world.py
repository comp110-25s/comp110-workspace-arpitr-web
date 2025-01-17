"""My first exercise in COMP110!"""

__author__ = "730698517"


def greet(name: str) -> str:
    """A welcome first function defination"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name?")))
