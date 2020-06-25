import sys
a = int(input())
score = sys.stdin.readline().split()
score = list(map(int, score))
answer = list(map(lambda x: x/max(score)*100, score))
print(round(sum(answer)/len(answer), 4))