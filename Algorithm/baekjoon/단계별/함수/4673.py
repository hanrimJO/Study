num_set = set(range(1, 10001))
kap_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    kap_set.add(i)

self_numset = num_set - kap_set
for i in sorted(self_numset):
    print(i)