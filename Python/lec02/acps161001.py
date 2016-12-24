lengths = [int(x) for x in input().strip().split()]
lengths.sort()
print(*length)

a, b, c = lengths
if a+b<=c:
    print('No')
elif a*a+b*b<c*c:
    print('Obtuse')
elif a*a+b*b>c*c:
    print('Acute')
else:
    print('Right')
