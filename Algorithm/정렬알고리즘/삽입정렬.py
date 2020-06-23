
a = [3, 5, 2, 7, 43, 25, 86, 32, 9]

for i in range(1, len(a)):
    for j in range(i, 0, -1):
        print(j)
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(a)
