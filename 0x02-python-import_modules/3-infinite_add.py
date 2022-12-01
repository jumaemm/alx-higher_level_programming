#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    sum_args = 0

    if argc == 0:
        print("0")
    else:
        for i in range(argc):
            sum_args += int(sys.argv[i + 1])
        print("{}".format(sum_args))
