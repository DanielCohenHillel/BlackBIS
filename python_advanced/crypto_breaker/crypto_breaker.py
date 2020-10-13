"""
Black Biss - Advance Python, Author: Daniel Cohen Hillel, ID: 212553804

Write a function that get a path to file that encrypted with 3 english-small-letter xor key, and print the
deciphered text.
"""
from itertools import product
from operator import xor


def crypto_breaker(file_path):
    with open(file_path, "r") as file:
        secret = [int(num) for num in file.read().split(",")]
        key_range = [range(97,123)]*3
        for key in product(*key_range):
            key *= len(secret)//3
            dec = map(xor, secret, key)
            for n, char in enumerate(dec):
                # Generator don't calculate their values until accessed, so I brea out of
                # the loop when I'm sure it's not the correct key so this would run faster
                # this destroys the first word of the message
                if char!=32:
                    if n>12:
                        break;
                    continue;
                elif n>12:
                    break;
                
                msg = "".join([chr(i) for i in dec])
                if all(len(m)<20 for m in msg.split(' ')):
                    # Generating back the first word of the message that was destroyd earlier
                    dec_d = map(xor, secret[:n+1], key[:n+1])
                    msg_d = "".join([chr(i) for i in dec_d])

                    print('\33[1m\33[4m\33[34mThe key is:\33[0m\n' + ''.join(map(chr, key)))
                    print('\n\33[1m\33[4m\33[34mThe message is:\33[0m\n' + msg_d + msg)



# small test to check it's work.
if __name__ == "__main__":
    crypto_breaker("big_secret.txt")
