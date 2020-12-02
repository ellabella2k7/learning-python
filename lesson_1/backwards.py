#!/usr/bin/python3
import sys

def backwards(phrase):
    count = 1
    esarhp = ''
    for _ in phrase:
        esarhp += phrase[-count]
        count += 1
    print(esarhp)

if __name__ == "__main__":
    try:
        backwards(phrase=sys.argv[1])
    except IndexError:
        print(
            'please provide word or phrase'
            '\n\nexample:\n\nbackwards "your phrase here!"'
        )