# #This is their example. Let's check it. Flag is all 0 for even numbers and 1 for odd numbers.
# flag=0
# num=eval(input('Enter a number: '))
# for i in range(2, num):
#     if num%i==0:
#         flag=1
#         break
#     print(i,flag)

# #1
# count=0
# for i in range (1,101):
#     x=i**2
#     if x%10==1:
#         print(x)
#         count=count+1
# print('There are ',count,'squares between 1 and 100 that ends with 1.')

# #2
# #For this example, how do I print the outcome of the squares side-by-side
# count=0
# count1=0
# for i in range (1,101):
#     x=i**2
#     if x%10==4:
#         count=count+1
#         print(x,'a')
#     # y=i**2
#     if x%10==9:
#         count1=count1+1
#         print(x)
# print('There are ',count,'and',count1,'squares between 1 and 100 that ends with 4 and 9 respectively.')

# #3
# from math import log
# n=eval(input('Enter a number: '))
# sum=0
# for i in range(1, n+1):
#     count=1/i
#     sum=sum+count
#     print(sum)
# y=sum-log(n)
# print(y)

# #4 one for loop then use mod
# s=0
# n=0
# for i in range (1,2000,2):
#     s=s+i
# print(s)
# for i in range (2,2001,2):  #for i in range (-2,-2001,-2):
#     n=n-i                         #n=n+i
# print(n)
# sum=s+n
# print(sum)

# 5
# sum=0
# x=eval(input('Enter a number: '))
# for i in range(1,x):
#     if x%i==0:
#         sum=sum+i       #sum+=i
#         print(i)        #I put this to confirm the divisi
# print('The sum of the divisible numbers is',sum)

# #6
# for x in range (1,10001):
#     sum=0
#     for i in range(1,x):
#         if x%i==0:
#             sum=sum+i       #sum+=i
#     if sum==x:
#         print(x, 'is a perfect number')

#7
# x=eval(input('Enter a number: '))
# flag=True
# for i in range(2,x):
#     if x%i==0:
#         #print (i)
#         y=int((i)**(1/2))
#         if y*y==i:
#             print(x,'is not squarefree')
#             flag=False
#             break
# if flag==True:
#     print(x,'is squarefree.')

# #8
# x= eval(input('Enter a number: '))
# y= eval(input('Enter a number: '))
# z= eval(input('Enter a number: '))
# print ('x=',x,'y=',y,'z=',z)
# x,y,z=y,z,x
# print(x,y,z)

# #9
# #Checking the math.ceil=math.floor method to know if a number is perfect square
# import math
# x=eval(input('Enter a number: '))
# y=math.sqrt(x)
# if math.ceil(y)==math.floor(y):
#     print (x, 'is a perfect square')
# else:
#     print(x, 'is not a perfect square')

# #solution9
"""
To check for the cube root, find the cube root of the number(x)
Then convert it to interger. Find the cube of the integer.
If it's equal to x, then it's a perfect cube.
"""
# import math
# sum=0
# sum1=0
# sum2=0
# for i in range(1,1001):
#     y=math.sqrt(i)
#     if math.ceil(y)==math.floor(y):
#         sum=sum+1
#     x=int((i)**(1/3))
#     if (x)**3==i:
#         sum1=sum1+1
#     y=int((i)**(1/5))
#     if (y)**5==i:
#         sum2=sum2+1
# sum0=1000-sum
# sum1_0=1000-sum1
# sum2_0=1000-sum2
# print(sum0,'numbers between 1 and 1000 are not perfect square.')
# print(sum1_0,'numbers between 1 and 1000 are not perfect cube.')
# print(sum2_0,'numbers between 1 and 1000 are not perfect fifth powers.')

# #10A CORRECTION NEEDED
# Largest_number=0
# for i in range(10):
#     num=eval(input('Enter number: '))
#     if num>Largest_number:
#         Largest_number=num
# print('Largest number: ',Largest_number)
# #OR
# sum=0
# number=eval(input('Enter first number: '))
# for i in range(9):
#     a=eval(input('Enter number: '))
#     sum=sum+a
#     if a>number:
#         number=a

# print('Largest number: ',number)
# for i in range(9):
#     if a<number:
#         number=a
# print('Smallest number: ',number)
# print('sum is', sum)    #To check
# average=sum/9
# print('The average is', average)
# if a>100:
#     print('Warning: A value entered is greater than 100')