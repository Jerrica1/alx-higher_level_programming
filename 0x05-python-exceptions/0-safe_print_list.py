#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
<<<<<<< HEAD
            printed += 1
        except:
            continue
    print()
    return printed
=======
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
>>>>>>> d4bd87ed20ea1e1867f5f96a80058eab7dffad53
