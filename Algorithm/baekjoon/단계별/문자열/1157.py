a = input().lower()
num_dict = {}

for i in a:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

num_dict.values()