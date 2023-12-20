#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_names = dir()
    for i in range(0, len(all_names)):
        if all_names[i][:2] != "__":
            print("{:s}".format(all_names[i]))
