row, col = [int(x) for x in input().split()]
picks = []
for i in range(row):
    picks.append(max([int(x) for x in input().split()]))

sums = sum(picks)
print(sums)

divisors = [x for x in filter(lambda x: sums % x == 0, picks)]

if divisors != []:
    print(*divisors)
else:
    print(-1)
