# x=eval(input('Enter length in cm: '))
# if x < 0:
#     print('Invalid Entry')
# else:
#     z=x/2.54
#     print('Length is equivalent to: ',z)

# x=eval(input('Enter temperature: '))
# y= input('Enter unit: ').lower()
# # y=y.lower()
# # note that, the input 'y' is case sensitive.
# F=(9*x/5)+32
# C=5*(x-32)/9
# if y=='celsius':
#     print('Temp in Fahrenheit is ',F)
# elif y=='fahrenheit':
#     print('Temp in Celsius is ',C)
# else:
#     print(y,'is not a valid unit.')


# temp=eval(input('Enter temperature in Celsius: '))
# if temp<-273.15:
#     print('The temperature is invalid because it is below absolute zero.')
# elif temp==-273.15:
#     print('The temperature is absolute 0.')
# elif -273.15<temp<0:
#     print('The temperature is below freezing.')
# elif temp==0:
#     print('The temperature is at the freezing point.')
# elif 0<temp<100:
#     print('The temperature is in the normal range.')
# elif temp==100:
#     print('The temperature is at the boiling point.')
# elif temp>100:
#     print('The temperature is above the boiling point')

# credit=eval(input('How many credit units have you taken: '))
# if credit<=23:
#     print('You are a freshman.')
# elif 24<=credit<=53:
#     print('You are a sophomore.')
# elif 54<=credit<=83:
#     print('You are a junior.')
# else:
#     print('You are a senior.')


# from random import randint
# x=randint(1,10)
# player=eval(input('Guess a number: '))
# if x==player:
#     print('Bravo!')
# else:
#     print('It is wrong, guess again.')
    

# items=eval(input('Enter number of items bought: '))
# if items<10:
#     cost=12*items
#     print('Total cost of items bought is ','$',cost,sep='')
# elif 10<=items<=99:
#     cost=10*items
#     print('Total cost of items bought is ','$',cost,sep='')
# elif items>=100:
#     cost=7*items
#     print('Total cost of items bought is ','$',cost,sep='')

# num1=eval(input('Enter the first number: '))
# num2=eval(input('Enter the second number: '))
# if round(abs(num1-num2),3)<=0.001:
#     print('Close')
# else:
#     print('Not close')

# year=eval(input('Enter year: '))
# if year%4==0 and year%100!=0:
#     print(year, ' is a leap year.',sep='')
# elif year%100==0 and year%400==0 and year%4==0:
#     print(year, ' is a leap year.',sep='')
# else:
#     print(year, ' is not a leap year.',sep='')
# #OR
# year=eval(input('Enter year: '))
# x=year/4
# y=year/100
# z=year/400
# if x-int(x)==0:
#     print(year, ' is a leap year.',sep='')
# elif y-int(y) and z-int(z)==0:
#     print(year, ' is a leap year.',sep='')
# else:
#     print(year, ' is not a leap year.',sep='')

#Not working
# x=eval(input('Enter a number: '))
# for i in range(1,x+1):
#     if x%i==0:
#         print(i)

# for i in range(1,11):
#     from random import randint
#     num1 = randint(1,10)
#     num2 = randint(1,10)
#     x=num1*num2
#     print('Question',i,': ',num1,' * ',num2,' = ',sep='',end='')
#     z=eval(input(''))
#     if z==x:
#         print('Right!')
#     else:
#         print('Wrong. The correct answer is ',x,'.',sep='')