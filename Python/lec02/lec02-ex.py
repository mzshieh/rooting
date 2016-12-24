while True:
    try:
        x = int(input()) # we ask for an integer
        break # if we got one, then we can stop
    except: # If we encounter any exception, we do the following
        print('Please give me an integer')

if x == 4:
    print('You give me four! God gives me five!')
elif x == 5:
    print('Give me five! Give you five!')
else:
    print('You give me '+str(x)+'!')
