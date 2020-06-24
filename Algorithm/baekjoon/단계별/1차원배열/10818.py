import sys
a = int(input())
b = sys.stdin.readline().split()
c = list(map(int, b))
print(min(c), max(c))

