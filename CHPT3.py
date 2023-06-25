# print ('The 50 random integers between 3 and 6 are: ')
# for i in range(50):
#     from random import randint
#     i = randint (3,6)
#     print(i, end=', ')

# from random import randint
# x = randint (1,50)
# y = randint (2,5)
# print (x,y)
# print (x**y)

# from random import randint
# x = randint (1,10)
# print (x)
# for i in range (x):
#     print ('SAMUEL S. NTUKIDEM')

# import random
# x = random.uniform (1,10)
# print (round(x,2))
#OR
# from random import uniform
# x = uniform (1,10)
# print (round(x,2))

# from random import randint
# w = randint(1,2)
# x = randint(1,3)
# z = randint(1,51)
# print (w, x, sep= ',', end=',')
# for i in range (47):
#     from random import randint
#     y = randint(1,50)
#     print ((y), end=',')
# print (z)

# x = eval(input('Enter the first number: '))
# y = eval(input('Enter the second number: '))
# w = x-y
# a = abs(w)
# b =a/(x+y)
# print(b)

#7 w = eval(input('Enter an angle between -180 and 180: '))

# x = eval(input('Enter the number of seconds: '))
# mins =x//60
# Sec =x%60
# print(x, 'seconds equal', mins, 'minute(s) and', Sec, 'second(s).')

# x = eval(input('Enter the hour between 1 and 12: '))
# y = eval(input('How many hours ahead: '))
# a = x+y
# b = a%12
# print('New hour: ',b,' o',"'",'clock',sep='')

# a=eval(input('Enter a power for 2: '))
# b= 2**a
# c=b%10
# print (b)
# print('The last digit of the above number is: ',c)

# a=eval(input('Enter a power for 2: '))
# b= 2**a
# c=b%100
# print (b)
# print('The last two digits of the above number is: ',c)

# a=eval(input('Enter a power for 2: '))
# b=eval(input('How many last didgit(s) do you want: '))
# c= 2**a
# d=10**b
# e=c%d
# print (c)
# print('The last', b, 'digits of the above number is: ',e)

# x = eval(input('Enter your weight in Kg: '))
# W = 2.2*x
# y= round(W,1)
# print('Your weight in pounds is', W)

# x = eval(input('Enter a number: '))
# from math import factorial
# print("factorial(",x,')= ',factorial(x),sep='')

# x = eval(input('Enter a number: '))
# from math import sin, cos, tan
# print("sin(",x,')= ',sin(x),sep='')
# print("cos(",x,')= ',cos(x),sep='')
# print("tan(",x,')= ',tan(x),sep='')

# x = eval(input('Enter an angle in degrees: '))
# from math import sin, radians
# print("sin(",x,')= ',sin(radians(x)),sep='')
#NOTE: The fxn 'radians' converts a number to degree

# sumi=0
# for i in range (0,350,15):
#     from math import sin, cos, radians
#     print(i,'---',sin(radians(i)), cos(radians(i)), sep=' ')
#     # sumi +=i
#     sumi=sumi+i
# print(sumi)


# C=eval(input('Enter the nth century (e.g. 19 for 19th century): '))
# Y=eval(input('Enter year(all four digits): '))
# m=(15+C-(C/4)-((8*C+13)/25))%30
# n=(4+C-(C/4))%7
# a=Y%4
# b=Y%7
# c=Y%19
# d=((19*c)+m)%30
# e=((2*a)+(4*b)+(6*d)+n)%7
# E = (22+d+e)
# F = (d+e-9)
# print(e)
# print(d)
# print('Easter is: ', 'March ',E, 'OR', 'April ', F,'.')
