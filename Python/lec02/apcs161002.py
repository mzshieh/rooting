row, col = [int(x) for x in input().split()]
rows = []
picks = []
for i in range(row):
    rows.append([int(x) for x in input().split()])
    picks.append(max(rows[-1]))

sums = sum(picks)
print(sums)
divisors = [x for x in filter(lambda x: sums % x == 0, picks)]
if divisors:
    print(*divisors)
else:
    print(-1)
