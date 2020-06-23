a = int(input())
tmp = 0
for i in range((2*a-1)):
    if i >= a:
        tmp -= 1
        print('*'*tmp)
    else:
        tmp += 1
        print('*'*(tmp))
