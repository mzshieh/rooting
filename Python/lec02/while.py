year = int(input('Give me a leap year: '))
while year % 400 != 0 and year % 100 == 0 or year % 4 != 0:
    print('No!!',year,'is not a leap year.')
    year = int(input('Give me a leap year: '))
    
print('Good!',year,'is a leap year.')