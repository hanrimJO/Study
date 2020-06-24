num_list = []
while True:
    try:
        a = int(input())
        num_list.append(a)
    except:
        break
max_num = max(num_list)
tmp = 0
for i in num_list:
    if i == max_num:
        print(max_num)
        print(tmp+1)
    else:
        tmp += 1
