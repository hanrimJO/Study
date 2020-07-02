a = input()

alpha = {
    'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1,
    'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1,
    'w': -1, 'x': -1, 'y': -1, 'z': -1,
}


for i in range(len(a)):
    if a[i] in list(alpha.keys()):
        if alpha[a[i]] == -1:
            alpha[a[i]] = i


num_list = list(alpha.values())
for i in num_list:
    print(i, end=' ')