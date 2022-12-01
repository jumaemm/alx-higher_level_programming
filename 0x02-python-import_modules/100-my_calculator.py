#!/usr/bin/python3

if __name__ == "main":
    from calculator_1 import add, sub, mul, div
    import sys
   
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    switch = {
            "+" : add(a, b),
            "-" : sub(a, b),
            "/" : div(a, b),
            "*" : mul(a, b)
            }
    if op not in switch:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("{} {} {} = {}".format(a, op, b, switch.get(op)))
