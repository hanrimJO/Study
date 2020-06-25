input_list = []
while True:
    try:
        a = int(input())
        input_list.append(a)
    except:
        break

divide = list(map(lambda x: x % 42, input_list))
print(len(set(divide)))

