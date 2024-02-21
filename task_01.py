def sum_num(list):
    return sum(list)


def max_num(list):
    return max(list)


def min_num(list):
    return min(list)


def list_sum_three_seven(list):
    return [i for i in list if i % 3 == 0 and i % 5 == 0]


def average_arithmetic(list):
    return sum(list) / len(list)

import random


start = random.randint(0, 10)
end = random.randint(20, 30)
list_num = [i for i in range(start, end)]

print(f"sum list: {sum_num(list_num)}\n"
      f"max number: {max_num(list_num)}\n"
      f"min number: {min_num(list_num)}\n"
      f"The sum of numbers that are divisible by 3 and 7: {list_sum_three_seven(list_num)}\n"
      f"average arithmetic: {average_arithmetic(list_num)}")
