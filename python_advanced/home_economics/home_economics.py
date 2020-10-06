"""
Black Biss - Advance Python

Write a function that calculate how many month one should save money to buy new car.
"""


def home_economics(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth):
    i = 0
    diff = startPriceOld - startPriceNew
    loss = 1 - percentLossByMonth / 100
    while (diff + i * savingPerMonth) < 0:
        diff *= loss
        loss -= 0.005 if i % 2 == 0 else 0
        i += 1
    return (i, round(diff + savingPerMonth * i))


# small test to check it's work.
if __name__ == "__main__":

    ret = home_economics(2100, 8000, 1000, 1.5)
    if ret[0] == 6 and ret[1] == 766:
        print("\33[1m\33[32mHAZA!\33[0m simple test pass :)")
    else:
        print("\33[1m\33[31mOops\33[0m, it's not working yet :(")
