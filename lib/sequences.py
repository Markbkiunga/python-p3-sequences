#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    numbers_list = []
    # print(dir(numbers_list))
    if length == 0:
        print(numbers_list)
        return
    if length >= 1:
        numbers_list.append(0)
    if length >= 2:
        numbers_list.append(1)
    for i in range(2, length):
        next_value = numbers_list[-1] + numbers_list[-2]
        numbers_list.append(next_value)
    print(numbers_list)


print_fibonacci(9)
