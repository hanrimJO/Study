h, m = map(int, input().split())

if m-45 > 0:
    m = m-45
    print(h, m)
elif m == 45:
    print(h, m-45)
else:
    if h == 0:
        h = 23
        tmp = 60 + (m - 45)
        print(h, tmp)
    else:
        h -= 1
        tmp = 60+(m-45)
        print(h, tmp)