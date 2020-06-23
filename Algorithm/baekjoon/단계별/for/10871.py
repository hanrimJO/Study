import sys
a, b = map(int, sys.stdin.readline().split())

answer = ''
c = list(map(int, sys.stdin.readline().split()))
for i in range(1, a+1):
    if c[i-1] < b:
        answer += (f"{c[i-1]} ")

print(answer.strip())