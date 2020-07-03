a = input().upper()
number = []
for i in set(a):
    number.append(a.count(i))

idx = [i for i, x in enumerate(number) if x == max(number)]

if len(idx) > 1:
    print('?')
else:
    print(list(set(a))[number.index(max(number))])