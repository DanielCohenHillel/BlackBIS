"""
Black Biss - Advance Python, Author: Daniel Cohen Hillel, ID: 212553804

Write a function that read one line from the user with many potentional passwords seperated by comma ","
and print out only the valid password - by the following rules:
    * contain letter from each of the characters-sets:
        lower-case english, upper-case english, decimal digit,
        special characters *&@#$%^
    * dosn't contain other symbols (ignore white-spaces)
    * length between 6 and 12

"""
import re

pattern = r"(?:,|^)(?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?=.*[*&^%$#@])([a-zA-Z\d*&^%$#@]{6,12}),"

def validate_passwords():
    passwords = re.findall(pattern, re.sub("\\s", "", input()))
    print("\33[1mValid passwords: \33[0m\33[35m", "\33[0m,\33[35m ".join(passwords))


# small test to check it's work.
if __name__ == '__main__':
    validate_passwords()
