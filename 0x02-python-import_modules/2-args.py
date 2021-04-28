#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)

    if count == 1:
        print("{}".format(count - 1), "arguments.")

    elif count == 2:
        print("{}".format(count - 1), "argument:")
        print("{}: {}".format(count - 1, argv[1]))

    else:
        for i in range(count):
            if i == 0:
                print("{} {}:".format(count - 1, "arguments:"))
            else:
                print("{}: {}".format(i, argv[i]))
