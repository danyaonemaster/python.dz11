import random

start = random.randint(0, 10)
end = random.randint(20, 30)
list_num = [i for i in range(start, end)]

print(f"sum list: {sum(list_num)}\n"
      f"max number: {max(list_num)}\n"
      f"min number: {min(list_num)}\n"
      f"The sum of numbers that are divisible by 3 and 7: {[i for i in list_num if i % 3 == 0 and i % 7 == 0]}\n"
      f"average arithmetic: {sum(list_num) / len(list_num)}")
