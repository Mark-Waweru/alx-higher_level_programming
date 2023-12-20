#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len == 1:
        print("{} argument:".format(arg_len), end="\n")
        print("{}: {}".format(1, sys.argv[arg_len]), end="\n")
    elif arg_len >= 1:
        print("{} arguments:".format(arg_len), end="\n")
        for i in range(1, arg_len + 1):
            print("{}: {}".format(i, sys.argv[i]), end="\n")
    else:
        print("{} arguments.".format(arg_len), end="\n")
