#explain break statement, continue statement and pass statement with example; (10 marks possible question in exam.)

# for i in range(10):
#     if (i==5):
#         break
#     print(i)
# print(" REST OF THE CODE ")

# for i in range(10):
#     if(i==5):
#         continue
#     print(i)
# else:
#     print("roc")

# i=1
# while i<=5:
#     print("multiverse")
#     i=i+1

# i=10
# while i>0:
#     print("2*",i,"=",i*2)
#     i-=1

# a=[1,2,3,4]
# sum=0
# i=0
# lists=len(a)
# while i<lists:,8,
#     sum=sum+a[i] 
#     i=i+1
# print(sum)

# a=[9,8,7,6]
# b=[]
# c=4
# while c>0:
#     c=c-1
#     b.append(a[c])
# print(b)


#HOMEWORK ask input again and again untill typed vowel letters
# letter=input('enter an alphabet; ')
# letter_lower=letter.lower()
# vowel=['a','e','i','o','u']
# while letter_lower in vowel:
#     print(f'{letter} is a vowel.')
#     break
# else:
#     print(f'{letter} is a consonant.')


# b=input("enter an alphabet; ")
# while(b!="a" and b!="e" and b!="i" and b!="o" and b!="u"):


# letter=input('enter an alphabet; ')
# letter_lower=letter.lower()
# vowel=['a','e','i','o','u']
# while letter_lower not in vowel:
#     letter=input("enter something")
# else:
#     print(f'{letter} is a vowel.')

# b=input("enter an alphabet; ")
# while(b!="a" and b!="e" and b!="i" and b!="o" and b!="u"):
#     b=input("try again")
# else:
#     print("this is a vowel")

# i=1
# while i<=10:
#     print(i)
#     i=i+1                                                         #changing or incrimental

i=1
while i<=10:
     
    if i==5:
        continue
    print(i)
    i=i+1
