level = int(input())
for i in range(level):
    print(' '*(level+1-i)+'*'*(2*i+1))
    print(' '*(level-i)+'*'*(2*i+3))
    print(' '*(level-1-i)+'*'*(2*i+5))
    
print(' '*(level+1)+'*')