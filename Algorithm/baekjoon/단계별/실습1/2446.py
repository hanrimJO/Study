a = int(input())
for i in range(a):
    print(' '*i+'*'*((a - i) * 2 - 1))
for i in range(a - 2, -1, -1):
    print(" " * i + "*" * ((a - i) * 2 - 1))