a = b = int(input())
count = 0

while True:
    ten = a // 10
    num = a % 10
    plus = ten + num
    count += 1
    a = int(str(num) + str(plus%10))
    if a == b:
        break
print(count)


