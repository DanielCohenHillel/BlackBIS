"""
Black Biss - Advance Python

Write a function that suggest which word is the Pirates meant to write.
"""


def dejumble(word, potentional_words):
    # write your code here
    pass


# small test to check it's work.
if __name__ == '__main__':

    ret = dejumble("orspt", ["sport", "parrot", "ports", "matey"])
    if len(ret) == 2 and set(ret) == set(["sport", "ports"]):
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")
