num = input('Give a number: ')
num_float = float(num)
if num_float < 0:
    # 負數
    num_ceil = int(num_float)
    num_frac = num_float - (num_ceil-1)
    if num_frac < 0.5:
        print(num_ceil-1)
    elif num_frac > 0.5:
        print(num_ceil)
    else:
        if num_ceil % 2 == 0:
            print(num_ceil)
        else:
            print(num_ceil-1)
elif num_float > 0:
    # 正數
    num_floor = int(num_float)
    num_frac = num_float - (num_floor)
    if num_frac < 0.5:
        print(num_floor)
    elif num_frac > 0.5:
        print(num_floor+1)
    else:
        if num_floor % 2 == 0:
            print(num_floor)
        else:
            print(num_floor+1)
else:
    # 0
    print(0)
