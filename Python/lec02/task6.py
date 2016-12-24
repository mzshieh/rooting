while True:
    x = input()
    try:
        int(x)
    except: # If we encounter any exception, we do the following
        print('Please give me an integer')
        continue
    if len(x) != 2:
        print('Please give me two digits')
    elif int(x) <= 0:
        print('Please give me a positive number')
    # elif x[0] == x[1]:
    elif int(x)//10 == int(x)%10:
        print('Please give me different digits')
    else:
        break

print(x,'is ok.')