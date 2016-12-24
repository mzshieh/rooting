row, col = [int(x) for x in input().strip().split()]

picks = []
for i in range(row):
    numbers = [int(x) for x in input().strip().split()]
    max_num = 1
    for num in numbers:
        if max_num < num:
            max_num = num
    picks.append(max_num)

sum_of_picks = 0
for pick in picks:
    sum_of_picks = sum_of_picks + pick
print(sum_of_picks)

divisors = []
for pick in picks:
    if sum_of_picks % pick == 0:
        divisors.append(pick)
if divisors==[]:
    print(-1)
else:
    print(*divisors)