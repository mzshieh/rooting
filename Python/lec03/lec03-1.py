def auto_boxing(x,y):
    return x, y

print(type(auto_boxing(1,2)),':',auto_boxing(1,2))

print('Auto unboxing a tuple')
a_tuple = (3,4)
a, b = a_tuple
print('a:',a,'& b:',b)

print('Auto unboxing a list')
a_list = [5,6]
c, d = a_list
print('c:',c,'& d:',d)