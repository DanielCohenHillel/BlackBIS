"""
Black Biss - Basic Python - Daniel Cohen Hillel, ID: 212553804

Write a function that remove all the odd values in  an array
"""


def odd_ones_out(in_array):
    return [i for i in in_array if i%2==0]


# small test to check it's work.
if __name__ == '__main__':
    arr_base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_expected = [0, 2, 4, 6, 8]

    if odd_ones_out(arr_base) == arr_expected:
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")
