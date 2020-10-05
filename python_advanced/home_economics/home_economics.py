"""
Black Biss - Advance Python

Write a function that calculate how many month one should save money to buy new car.
"""


def home_economics(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth):
    # write your code here
    pass


# small test to check it's work.
if __name__ == '__main__':

    ret = home_economics(2000, 8000, 1000, 1.5)
    if ret[0] == 6 and ret[1] == 766:
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")
