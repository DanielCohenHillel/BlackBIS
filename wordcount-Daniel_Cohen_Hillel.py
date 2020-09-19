import sys

def print_words(filename):
    print("print_words")

def print_top(filename):
    print("print_top")


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
