n = int(input('Please type a number you want to convert: '))
ans = ''
base = int(input('Please type the base to which it should be converted: '))
while base > 36:
    base = int(input('The base needs to be lower than 37 please reinput your base:'))
while n > 0:
    temp = n % base
    if temp <= 9:
        ans = str(temp) + ans
    elif temp > 9:
        ans = chr(55 + temp) + ans
    n = n // base
print('Your number in base '+str(base) + ' is equal to '+ans)
