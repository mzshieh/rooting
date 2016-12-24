line = input('Give me some years: ')
years = [int(x) for x in line.strip().split()]
num = len(years)
for i in range(num):
    year = years[i]
    if year % 400 == 0 or year % 100!=0 and year % 4==0:
        print(year,'is a leap year.')
    else:
        print(year, 'is not a leap year.')