# list=[]
# size=int(input('Enter the number of integers: '))
# for i in range(size):
#     print('Enter number for ',i)
#     l=int(input())
#     list.append(l)
# print('The list of integer is ',list)

# #1
# print('The total number of item in the list is ', len(list))
# print('The last item in the list is ',list[len(list)-1])
# list.reverse()          #I tried storing it in a variable, it's not printing. OR reverse_list=list[::-1]
# print('The reverse list is ',list)
# n='5'
# count=0
# for n in list:
#     if list.index(n):
#         print ('Yes')       #It says no 5 in the list, but there is.
#         count+=1
#     else:
#         print ('No')
# print('The number of fives are', count)
# list.remove(list[0] and list[len(list)-1])      #This removes only the last
# print(list)
# list.sort()
# print(list)
# integer=0
# for i in list:
#     if i>5:
#         integer+=1
# print ('There are',integer,'integer(s) greater than 5.')

#2 Why is this generating only one number?
# from random import randint
# for i in range(20):
#     random=[randint(1,101)]
# print(random)

# #2
# L=[]
# from random import randint
# for i in range(20):
#     L=L+[randint(1,101)]
#     #L.append(randint(1,101))
# print(L)
# print('The average of the list above is',sum(L)/len(L))
# largest_num=L[0]
# smallest_num=L[0]
# count=0
# for i in L:         #loop method is not working
#     if i>largest_num:
#         largest_num=i
#     if i<smallest_num:
#         smallest_num=i
#     if i%2==0:
#         count+=1
# print(largest_num)
# print(smallest_num)
# print('The largest and smallest values in the list are',largest_num,'and',smallest_num,'respectively.')
# #OR sort method
# L.sort()
# print('The largest and smallest values in the list are',L[len(L)-1],'and',L[0],'respectively.')
# print('There are',count,'even number(s) in the list above.')

# #3
# L=[8,9,10]
# #L=L.replace(1,17)      This doesn't work, why?
# L[1]=17
# print(L)
# L=L+[4,5,6]
# del L[0]
# L.sort()
# print(L)
# L=L*2
# print(L)
# # doubled=[]
# # for i in L:                      #for i in range(len(L))
# #     doubled.append(i+i)          #i=i*2
# # print(doubled)
# L=L[:3]+[25]+L[3:]   #what is the difference between L[:3] and L[3:]?
# print(L)

# #4
# n=eval(input('Number of entry: '))
# list=[]
# for i in range(1,n+1):
#     print('Enter number for',i,'not greater than 12: ')
#     num=int(input())
#     if num>12:
#         print('The number entered is greater than 12')
#         continue    #how do I repeat the line of loop when entery is greater than 12?
#     else:
#         list.append(num)
# print(list)
# for i in list:
#     if i>10:
#         list[list.index(i)]=10
# print(list)

# #5
# n=eval(input('Number of entry: '))
# list=[]
# for i in range(1,n+1):
#     print('Enter the strings: ')
#     words=str(input())
#     list.append(words[1:])
# print(list)

# #6
# L=[]
# square=[]
# alphabet=[]
# alpha=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
# for i in range(50):
#     num=int(i)
#     L.append(num)
#     sqr=(i+1)**2
#     square.append(sqr)
#     if i<=25:
#         c=alpha[i]*(i+1)
#         alphabet.append(c)
# print(L)
# print(square)
# print(alphabet)

# # 7
# L=[]
# M=[]
# N=[]
# size=eval(input('Enter list size: '))
# for i in range(size):
#     l=int(input('Enter element for L: '))
#     L.append(l)
#     m=int(input('Enter element for M: '))
#     M.append(m)
#     n=L[i]+M[i]
#     N.append(n)
# print(L)
# print(M)
# print(N)
# # p=[int(i) for i in input('Enter the elememnt of list: ').split()]
# # For this ex. I learnt about N = list(map(add, L, M))
# # Also N = [sum(i) for i in zip(L, M)]......N = [a+b for a, b in zip(L, M)]
# # Finally, operator* method

#8
# num=int(input('Enter a number: '))
# L=[]
# for i in range(1,num+1):
#     if num%i==0:
#         L.append(i)
# print('The list for the factors of',num,'are: ', L)

#9
# count2=0            #list of 12 0s
# count3=0
# count4=0
# count5=0
# count6=0
# count7=0
# count8=0
# count9=0
# count10=0
# count11=0
# count12=0
# T_outcomes=[]
# T=[0]*11
# print(T)
# percentage=[]
# from random import randint
# for i in range (10000):
#     x=randint(1,6)
#     y=randint(1,6)
#     outcome=x+y
#     print(outcome)
#     print(T[outcome-1])
#     T[outcome-1]=T[outcome-1]+1
#     if outcome==2:
#         count2+=1
#     elif outcome==3:
#         count3+=1
#     elif outcome==4:
#         count4+=1
#     elif outcome==5:
#         count5+=1
#     elif outcome==6:
#         count6+=1
#     elif outcome==7:
#         count7+=1
#     elif outcome==8:
#         count8+=1
#     elif outcome==9:
#         count9+=1
#     elif outcome==10:
#         count10+=1
#     elif outcome==11:
#         count11+=1
#     elif outcome==12:
#         count12+=1 
# T_outcomes.append(count2)
# T_outcomes.append(count3)
# T_outcomes.append(count4)
# T_outcomes.append(count5)
# T_outcomes.append(count6)
# T_outcomes.append(count7)
# T_outcomes.append(count8)
# T_outcomes.append(count9)
# T_outcomes.append(count10)
# T_outcomes.append(count11)
# T_outcomes.append(count12)
# print('The number of occurences for 2 to 12 respectively are: ',T_outcomes,T)#T
# for i in T_outcomes:
#     percent=100*i/10000
#     percentage.append(percent)
# print('The percentages for the occurences of 2 to 12 respectively are: ',percentage)

#10
# list=[]
# size=int(input('Enter the number of element: '))
# for i in range(size):
#     print('Enter number for ',i)
#     l=eval(input())
#     list.append(l)
# print('Original list: ',list)
# list_1= list[1:]+[list[0]]  
# print('Rotated list: ',list_1)
#OR
# list=[3,5,6,4,9]
# list1=list[1:]
# list2=[list[0]]
# list=list1+list2
# print(list)