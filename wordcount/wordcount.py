import sys
from collections import Counter
import re
from string import punctuation

def get_words(filename):
    filestr = open(filename, 'r').read().lower()
    return re.sub(f'[{punctuation}]', '', filestr).split()

def print_words(filename):
    word_count = sorted(Counter(get_words(filename)).items())
    for word_tup in word_count:
        print(('\33[1m{}\33[0m'+'.'*(15-len(word_tup[0]))+'{}').format(*word_tup))

def print_top(filename):
    word_count = sorted(Counter(get_words(filename)).items(), key=lambda x: x[1], reverse=True)
    for i in range(20):
        print(('\33[1m{}\33[0m'+'.'*(15-len(word_count[i][0]))+'{}').format(*word_count[i]))

def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | ---topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)

    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
