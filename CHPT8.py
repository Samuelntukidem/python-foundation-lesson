# #1
# article=['a','an','the']
# text=input("Enter a text: ")
# text=text.lower()
# split_text=text.split()
# print(split_text)
# count1=split_text.count(article[0]) + split_text.count(article[1]) +split_text.count(article[2])
# print('There are',count1,'article(s) in the text.')
# #OR
# count=0
# for item in split_text:
#     if item.lower() in article:
#         count+=1
# #OR
# L=sum([1 for item in split_text if item.lower() in article])
# print(L)

#2
# L=[]
# for i in range(5):
#     Numbers=input('Enter the number: ')
#     L.append(Numbers)
# x='+'.join(L)
# print(x)

# l=[i for i in range(5) Numbers=input('Enter the number: ')]   #This syntax doesn't work

#3
# sent=input('Enter a sentence: ')
# s=sent.split()
# print('The third word in the sentence is,',s[2])
# for i in s[2]:
#     print(i, end=',')

# #4a
# from random import shuffle
# sent=input('Enter a sentence: ')
# s=sent.split()
# shuffle(s)
# s_shuffled=' '.join(s)
# print(s_shuffled)
# #4b
# from random import shuffle
# sent=input('Enter a sentence: ')
# s=sent.split()
# shuffle(s)
# s_shuffled=' '.join(s)
# #print(s_shuffled[0].upper())
# print(s_shuffled.capitalize())

# #5
# from random import choice
# daily_quotes=['you are blessed','God is with you', 'God is the greatest']
# print('The quote for today is:', choice(daily_quotes))

#6
# from random import randint
# lottery=[randint(1,48) for i in range(6)]
# print('Your lottery draw numbers are:',lottery)
#OR
# lottery=[]
# from random import randint
# for i in range(6):
#     lottery.append(randint(1,48))
# print('Your lottery draw numbers are:',lottery)
# OR
# from random import sample
# lottery_number=sample(range(1, 49), 6)
# print (lottery_number)

# #7
# from random import randint
# lottery=[randint(1,10) for i in range(1000)]
# print (lottery)

#8

#9
# count=0
# questions=['what is your name?', 'how old are you?', 'what is your middle name?', 'what is your first name?', 'what is your last name?']
# answers=['edna','12', 'kemi', 'femi', 'ola']
# from random import sample
# exam=[sample(questions, 4)]
# for i in questions:
#     for c in exam:
#         if exam[c]==questions[i]:
#             print(c)
#     user_answer=input('what is your answer: ')
#     if user_answer.lower()==answers[questions.index(i)]:
#         print('Your answer is correct.')
#         count+=1
#     else:
#         print('Your answer is wrong.')
# print('You got',count,'out of 4.')

#10
# curse=['darn','dang','freakin','heck','shoot']
# text=input('Enter text: ')
# for c in curse:
#     if c in text.lower():
#         curse_detected=text.replace(c,'*'*len(c))
# print(curse_detected)
# #if any([c in text for c in curse]):  ANOTHER METHOD TO SEARCH
# # The below(102-109) is for the situation when both the text and curse word is inputted 
# #word_list = text.split()
# #replaced_word = '*' * len(curse)
# #for i in range(len(word_list)):
# #   if word_list[i] == curse:
# #      word_list[i] = replaced_word
# #final_string = ' '.join(word_list)
# #print("The sentence is : ", text)
# #print("Replacement with asterisks is as shown : ",final_string)
# ########
# text_list=text.split() 
# replaced_CurseWord = '*' * len(curse)  
# for i in range(len(text_list)):
#     if text_list[i] == curse:
#       text_list[i] = replaced_CurseWord
# final_text = ' '.join(text_list)
# print("The sentence is : ", text)
# print("Replacement with asterisks is as shown : ",final_text)

#11
# from random import choice
# word = input('Enter a word: ')
# for i in range(len(word)):
#     print(choice(word), end='')     #Can I store it and make it a print statement.

#12
# number=input('Enter your phone number separated with dash(-): ')
# for c in number:
#         if c==' ':
#             print('Invalid')
# numbers=number.split('-')
# if len(numbers)==4:
#     num1=numbers[0]
#     num2=numbers[1]
#     num3=numbers[2]
#     num4=numbers[3]
#     if num1.isalnum() and len(num1)!=1:
#         print('Invalid')
#     elif num2.isalnum() and len(num2)!=3:
#         print('Invalid')
#     elif num3.isalnum() and len(num3)!=3:
#         print('Invalid')
#     elif num4.isalnum() and len(num4)!=4:
#         print('Invalid')
#     for x in num1:
#         if x!='1':
#             print('Invalid')
#     print('valid')
# if len(numbers)==3:
#     num1=numbers[0]
#     num2=numbers[1]
#     num3=numbers[2]
#     if num1.isalnum() and len(num1)!=3:
#         print('Invalid')
#     elif num2.isalnum() and len(num2)!=3:
#         print('Invalid')
#     elif num3.isalnum() and len(num3)!=4:
#         print('Invalid')
#     print('valid')
# else:
#     print('Valid')


# #5x5x5
# from pprint import pprint
# L = [[[0]*5 for i in range(5)] for j in range(5)]
# pprint(L)

# for r in L:
#     print(r)
#     for c in range(5):
#         print(L[r][c], end=" ")
#     print()