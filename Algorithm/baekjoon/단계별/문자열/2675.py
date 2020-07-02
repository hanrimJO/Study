import sys
cnt = int(input())

for i in range(cnt):
    a = sys.stdin.readline().split()
    number = int(a[0])
    alpha = list(a[1])
    answer = ''
    for j in range(len(a[1])):
        answer += alpha[j]*number

    print(answer)
