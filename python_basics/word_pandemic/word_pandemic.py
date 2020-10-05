"""
Black Biss - Basic Python - Daniel Cohen Hillel, ID: 212553804

Write a function that replace any second word with the word "Corona".
"""


def word_pandemic(in_array):
    return " ".join([word if i%2==0 else 'Corona' for i, word in enumerate(in_array.split(' '))])


# small test to check it's work.
if __name__ == '__main__':
    base_word = "Koala Bears are the cutest"
    sick_word = "Koala Corona are Corona cutest"

    if word_pandemic(base_word) == sick_word:
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")