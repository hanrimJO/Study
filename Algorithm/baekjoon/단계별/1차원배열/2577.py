a = int(input())
b = int(input())
c = int(input())
abc = list(str(a * b * c))
num_list = {}
for i in abc:
    if str(i) in num_list:
        print(c[str[i]])
        c[str(i)] += 1
    else:
        num_list[i] = 1
print(num_list)