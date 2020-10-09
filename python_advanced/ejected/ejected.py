"""
Black Biss - Advance Python, Author: Daniel Cohen Hillel, ID: 212553804

Write a function that calculate how far is our ejected pilot.
Run this program and insert the following lines (each end with Enter):

UP 5
DOWN 3
LEFT 3
RIGHT 2
0

and the result should be 2
"""
import traceback

move = {"right": 1, "left": -1, "up": 1j, "down": -1j}


def ejected():
    """Calculate how far is our ejected pilot.
    Input to stdin UP/DOWN/RIGH followd by a space and the number of steps in that
    direction     repeatedly, when you want to eject, enter '0' and off you go ;)"""

    position = 0 + 0j
    while True:
        inp = input()
        if inp == "0":
            break
        try:
            direction, steps = inp.lower().split(" ")
            position += move[direction] * float(steps)
        except ValueError:
            traceback.print_exc()
            print('\33[1m\33[31mInput must be of the form:\n>    \33[33m`direction float`\33[0m')
        except KeyError:
            traceback.print_exc()
            print('\33[1m\33[33m'+direction, '\33[0mis not a valid direction!')

    return round(abs(position))


# small test to check it's work.
if __name__ == "__main__":
    print("The pilot is vibing\33[1m\33[34m", ejected(), "units\33[0m away from the origin🌴")
