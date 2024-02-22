input_num = int(input("Enter a number: "))
input_symbol = input("Enter a symbol: ")

if input_num == 0:
    print()
    exit()

print(input_symbol * input_num)
if input_num == 1:
    exit()

if input_num != 2:
    for i in range(input_num -2):
        print((" " * (input_num - 2)).join([input_symbol]*2))

print(input_symbol * input_num)