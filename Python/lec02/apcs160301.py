line = input()
n = int(line)
scores = [int(x) for x in input().strip().split()]
scores.sort()
print(*scores)

luck = 101
for x in scores:
    if x >= 60 and x < luck:
        luck = x

unluck = -1
for x in scores:
    if x < 60 and x > unluck:
        unluck = x

if unluck == -1:
    print('best case')
else:
    print(unluck)

if luck == 101:
    print('worst case')
else:
    print(luck)
