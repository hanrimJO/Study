a = int(input())
b = int(input())
c = int(input())
abc = list(str(a * b * c))
num_list = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in abc:
    if str(i) in num_list:
        num_list[str(i)] += 1
    else:
        num_list[i] = 1
number = list(num_list.values())
for i in number:
    print(i)