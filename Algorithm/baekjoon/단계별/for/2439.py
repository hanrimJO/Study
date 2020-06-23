a = int(input())

for i in range(1, a+1):
    space = ' '
    star = '*'
    print(space*(a-i)+star*i)