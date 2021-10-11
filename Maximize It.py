from itertools import product

k, m = map(int,input().split())
lists = []
results = []

for _ in range(k):
    temp_length, temp_list = input().split(maxsplit=1)
    length = int(temp_length)
    lists.append(list(map(int,temp_list.split())))

all_combinations = list(product(*lists))

for i in all_combinations:
    results.append(sum([x**2 for x in i])%m)

print(max(results))
