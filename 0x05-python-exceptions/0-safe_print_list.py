#!/usr/bin/python3


def safe_print_list(my_list=(1, x=0)):
    i = 0
    printed = 0
    for i in range(0, x):
        try:
            printed += 1
            print("({})".format(my_list[i]), end="")
        except:
            continue
        print()
        return printed
