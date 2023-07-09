#1
# i=0
# while i<50:
#     i=i+1
#     print(i, end=' ')

#2a
# string=input('Enter a string: ')
# i=0
# while i<len(string):
#     print (string[i])
#     i=i+1
#2b
# string=input('Enter a string: ')        #NOT CORRECT
# i=0
# while i<len(string):
#     print (string[1])
#     i=i+1

#3
# weight=eval(input('Enter weight in Kg: '))
# while weight<0:
#     weight=eval(input('The weight entered is invalid. Enter weight again in Kg: '))
# print(weight,'Kg is equivalent to', weight*2.205, 'pounds')

#4
# i=1
# pw='goodLORD'
# password=input('Enter your correct password: ')
# while pw!=password and i<5:
#     print(input('Incorrect password. Please, enter the correct password: '))
#     i=i+1
# if pw==password:
#         print('You are logged in to the system')
# else:
#       print('You are kicked off of the system')

#5
# scores=[]
# i=0
# count=0
# print('Input your test score and end with a negative value')
# while i>=1:
#     test_scores=int(input('Enter your test scores: '))
#     i=i+1
#     scores.append(test_scores)          #append is not working in the while loop. Why?
# print(scores)
# if test_scores<0:
#     print('You are done entering your test scores.')
#     break
# if test_scores>=90:
#     count+=1    
#     print ("The number of A's gotten are",count)
# print('The average score is', sum(scores)/len(scores))

#6
# from random import randint
# secret_num = randint(1,100)
# num_guesses = 0
# guess = 0
# while guess != secret_num and num_guesses <= 4:
#     guess = eval(input('Enter your guess (1-100): '))
#     num_guesses = num_guesses + 1
#     guess_left=5-num_guesses
#     if guess_left<=1 and guess != secret_num:
#         if guess < secret_num:
#             print('HIGHER.', guess_left, 'guess left.\n')
#         elif guess > secret_num:
#             print('LOWER.', guess_left, 'guess left.\n')
#     elif guess < secret_num:
#         print('HIGHER.', guess_left, 'guesses left.\n')
#     elif guess > secret_num:
#         print('LOWER.', guess_left, 'guesses left.\n')
#     else:
#         print('You got it!')
# if num_guesses==5 and guess != secret_num:
#     print('You lose. The correct number is', secret_num)

#7
#7a - how does while loop come into play here?
#7b
# string=input('Enter a text: ')
# letter=input('Enter a letter: ')
# for c in string:
#     if c==letter:
#         print (string.index(letter))
#     elif c not in string:
#         print('No', letter, 'in', string)
#     else:
#         break

#8 It only works for 42 and 18
# num1=eval(input('Enter the larger number: '))
# num2=eval(input('Enter the smaller number: '))
# while num1<num2:
#     num1=eval(input('Enter the larger number again: '))
#     num2=eval(input('Enter the smaller number: '))
# remainder1=num1%num2
# remainder2=num2%remainder1
# while remainder2!=0:
#     remainder2=num2%remainder1  #How do I make this line keep repeating with the new remainders?
# if remainder2==0:
#     print(remainder1,'is the GCD of',num1,'and',num2)

#9
num1=eval(input('Enter the larger number: '))
guess=eval(input('Enter the larger number: '))