
a = [3, 4, 5, 2, 34, 9, 67, 25, 12]

for i in range(1, len(a)):
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

