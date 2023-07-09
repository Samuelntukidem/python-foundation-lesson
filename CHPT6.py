# s = ''
# for i in range (10):
#     t=input('Enter a letter: ')
#     if t=='a' or t=='e' or t=='i' or t=='o' or t=='u':
#         s = s + t
# print (s)

# #1
# s=input('Enter a text: ')
# print('The total number of characters in the string is',len(s))
# print(s*10, sep=', ')
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# if len(s)>=7:
#     print(s[6])
# else:
#     print('The characters inputed are not upto 7')
# print(s[1:len(s)-1])
# print(s.upper())
# print(s.replace('a','e'))
# print(s.index('e')) #I added this just to find the position of 'e' in arise following line22
# #Why is the result 4 and not 0
# ans=''
# for c in s:                 #I dont know what kinda loop I did here.
#     if c.isalpha():
#         ans=ans+' '
#     else:
#         ans=ans+c
# print(ans)

# #2
# count=0
# for c in s:
#     if c==' ':
#         count=count+1
# print(count)
# words=count+1
# print('The total number of words is',words)
# #OR
# x=s.count(' ')
# words=x+1
# print('The total number of words is',words)

#3
# count1=0
# count2=0
# formula=input('Enter the formula:')
# for c in formula:
#     if c=='(':
#         count1=count1+1
#     if c==')':
#         count2=count2+1
# if count1!=count2:
#     print('The number of parentheses entered are not even')
# else:
#     print('The formula is okay.')

#4                        Flag can work here
# count=0
# Word=input('Enter a word:')
# Word=Word.lower()
# for c in Word:
#     if c in 'aeiou':
#         count=count+1
# if count>0:
#     print('The word you entered contains a vowel.')

#5
# K=input('Enter a word:')
# W=K[0]+'*'+K[2:]+'!!!'
# print(W)

#6
# S=input('Enter a word:')
# S=S.lower()
# for c in ',':               #I only used comma
#     S=S.replace(c,'')
# print (S)

#7
# Word=input('Enter a word: ')
# Reverse=Word[::-1]
# if Word==Reverse:               #what's wrong with this if statement?
#     print(Word,'is a palindrome')
# else:
#     print(Word,'is not a palindrome')

#8      #Not Correct
# numE=eval(input('Enter number of email address(s): '))
# s='@student.college.edu'
# p='@prof.college.edu'
# count1=0
# count2=0
# for i in range(numE):
#     address=input('Email address: ')
#     if p in address:
#         count1=count1+1
#     else:
#         count2=count2+1
# if count1==0:
#     print('All addresses are student addresses.')
# elif count2==0:
#     print('All addresses are profs addresses.')
# else:
#     print('There are',count1,'professor addresses entered and',count2,'student addresses in the school.')


#9
# num=eval(input('Enter a number: '))
# for i in range(num):
#     print(' '*i,i+1)

#10
# word=(input('Enter a word: '))
# for i in range(len(word)):
#     print(word[i]*2)

#24
# n=eval(input('Enter the power: '))
# y=(input('Enter the variable: '))
# print(y,'^',n)
# print('The differential is ',n,y,'^',n-1,sep='')