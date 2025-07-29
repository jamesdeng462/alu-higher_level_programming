def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")  # print elements in one line
            count += 1
    except IndexError:
        pass  # stop when we reach the end of the list
    print()  # new line after printing all items
    return count
