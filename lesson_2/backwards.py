#!/usr/bin/python3

"""
Import allows the use of other python scripts called modules to use in your
own code without having to write the extra code.
"""
import sys


def cap(phrase):
    print(phrase.upper())

"""
'def' is for defining a function. ex def name():
the function can accept arguments if any are given.
the function acts as a set of actions or a single action to be completed.
"""
def backwards(phrase):
    count = 1 # int type(1) <class='int'>
    esarhp = ''
    for _ in phrase:
        esarhp += phrase[-count]
        count += 1
    # if input("Uppercase: (y/N)\n") == "y":
    #     cap(esarhp)
    # else:
    #     print(esarhp)
    print(esarhp)


if __name__ == "__main__":
    # backwards(phrase=sys.argv[1])
    try:
        # backwards(phrase="hello world")
        backwards(phrase=sys.argv[1])
    except IndexError:
        print(
            'please provide word or phrase'
            '\n\nexample:\n\nbackwards "your phrase here!"'
        )
