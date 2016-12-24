level = int(input())
maxlen = (level+2) * 2 - 1
for i in range(level):
    print(('*'*(2*i+1)).center(maxlen))
    print(('*'*(2*i+3)).center(maxlen))
    print(('*'*(2*i+5)).center(maxlen))
print('*'.center(maxlen))
print('*'.center(maxlen))
