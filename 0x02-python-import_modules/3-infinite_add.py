#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    result = 0

    for i in range(1, count):
        result += int(argv[i])
print(result)
