"""
Black Biss - Advance Python

Write a function that get array of string, each represent a row in 2-dim map, when:
    'X' is start / destination point
    '-' is road right-left
    '|' is road up-down
    '+' is a turn in the road, can be any turn (which isn't continue straight)
    path = ["           ",
            "X-----+    "
            "      |    "
            "      +---X",
            "           "]

    # Note: this grid is only valid when starting on the right-hand X, but still considered valid
    path = ["                      ",
            "   +-------+          ",
            "   |      +++---+     ",
            "X--+      +-+   X     "]
    nevigate_validate(path)  # ---> True
"""


def nevigate_validate(path):
    # write your code here
    pass
    return True


# small test to check it's work.
if __name__ == '__main__':
    path = ["           ",
            "X-----+    "
            "      |    "
            "      +---X",
            "           "]
    valid = nevigate_validate(path)

    path = ["           ",
            "X--|--+    "
            "      -    "
            "      +---X",
            "           "]
    invalid = nevigate_validate(path)
    if valid and not invalid:
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")
