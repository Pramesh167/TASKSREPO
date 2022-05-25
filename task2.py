# #1. What is the output of ‘banana’ > ‘BANANA’?
# a="banana"
# print(a)
# print(a.upper())

#2. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]

# a=int(input("Enter a number to check weather the number is natural or not:"))
# if a>=0:
#     print("The given number is natural.")
# else:
#     print("The given number is not natural number.")

#3. Given three integers, print the smallest one. (Three integers should be user input)

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number: "))
#
# if a<b and a<c:
#     print("The smallest number is a which is",a)
# elif b<a and b<c:
#     print("The smallest number is b which is",b)
# else:
#     print("The smallest number is c which is",c)

#4. Given a three-digit number. Find the sum of its digits

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number: "))
# sum=a+b+c
# print("The sum of number is:",sum)

#5. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where
# 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number
# that is outside the range of 1 to 12.

# month=int(input("Enter a number to know month:"))
# if month==1:
#     print("January")
# elif month==2:
#     print("February")
# elif month==3:
#     print("March")
# elif month==4:
#     print("April")
# elif month==5:
#     print("May")
# elif month==6:
#     print("June")
# elif month==7:
#     print("July")
# elif month==8:
#     print("August")
# elif month==9:
#     print("September")
# elif month==10:
#     print("October")
# elif month==11:
#     print("November")
# elif month==12:
#     print("December")


#6. Given x = 5, what will be the value of x after we run x+=3?

# x=5
# x+=3
# print(x)

#7. Write a Python Program to Check Prime Number.
# a=int(input("Enter a number to check weather the given number is prime or not:"))
# b=3
# if a%b==0:
#     print("prime number")
# else:
#     print("composite numbers")

#8.8. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# math=int(input("Enter your marks in math:"))
# programming=int(input("Enter your marks in programming:"))
# science=int(input("Enter your marks in science:"))
# english=int(input("Enter your marks in english:"))
# totalmarks=400
# obtainedmarks=math+programming+science+english
# percentage=obtainedmarks/totalmarks*100
# print("Your percentage is:",percentage)
# if percentage>80:
#     print("you got A")
# elif percetage>60:
#     print("you got B")
# elif percentage>50:
#     print("you got C")
# elif percentage>45:
#     print("you got D")
# elif percentage>25:
#     print("you got E")
# else:
#     print("you got F")

#9. Take input of age of 3 people by user and determine oldest and youngest among them
# a=int(input("Enter your age:"))
# b=int(input("Enter your age:"))
# c=int(input("Enter your age:"))
# if a>b and a>c:
#     print("A is oldest")
# elif b>c and b>a:
#     print("B is oldest")
# elif c>a and c>b:
#     print("C is oldest")
# if a<b and a<c:
#     print("A is youngest")
# elif b<a and b<c:
#     print("B is youngest")
# else:
#     print("C is youngest")

# 10.  Write a program to check whether a person is eligible for voting or not. (accept age from user)

# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible for voting.")
# else:
#     print("sorry you are not eligible for voting.")

#11.  Write a program to check whether a number entered by user is even or odd.

# a=int(input("Enter a number to check the number is even or odd:"))
# if a%2==0:
#     print("Even number.")
# else:
#     print("Odd number.")

#12. Write a program to check whether a number is divisible by 7 or not.

# a=int(input("Enter a number to check weather it is divisible by 7 or not:"))
# if a%7==0:
#     print("The number you entered is divisible by 7")
# else:
#     print("Sorry!!")


#13. Write a program to display "Hello" if a number entered by user is a multiple of five ,
# otherwise print "Bye".

# n=int(input("Enter a number:"))
# if n%5==0:
#     print("Hello")
# else:
#     print("Bye")

#14. Write a program to accept percentage from the user and display the grade according to the following criteria:

         # Marks                                    Grade
         # > 90                                         A
         # > 80 and <= 90                    B
         # >= 60 and <= 80                  C
         # below 60                                 D

# totalmarks=400
# english=int(input("Enter your marks in english:"))
# math=int(input("Enter your marks in math:"))
# computer=int(input("Enter your marks in computer:"))
# account=int(input("Enter your marks in account:"))
# obtainedmarks=english+math+computer+account
# print("Your obtained marks is:",obtainedmarks)
#
#
# percentage=obtainedmarks/totalmarks*100
# print("Your percentage is:",percentage)
#
# if percentage>90:
#     print(" A")
# elif percentage>80:
#     print(" B")
# elif percentage>=60:
#     print(" C")
# else:
#     print(" D")

# 15. Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal

# city=input("Enter the name of the city:")
# if city=="Delhi":
#     print("Red Fort")
# elif city=="Agra":
#     print("Taj Mahal")
# elif city=="Jaipur":
#     print("Jal Mahal")

#16. Write the output of the following if

# a = 9
#
# if (a>5  and a<=10):
#     print("Hello")
# else:
#     print("Bye")

#17. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

# num = int(input("enter number:"))
# if num%2 == 0:
#    if num%3 == 0:
#       print ("Divisible by 3 and 2")
#    else:
#       print ("divisible by 2 not divisible by 3")
# else:
#    if num%3 == 0:
#       print ("divisible by 3 not divisible by 2")
#    else:
#       print  ("not Divisible by 2 not divisible by 3")

# 18. Write a program to check a character is vowel or not.

# n=input("Enter one letter:")
# if n=="a":
#     print("vowel")
# elif n=="e":
#     print("vowel")
# elif n=="i":
#     print("vowel")
# elif n=="0":
#     print("vowel")
# elif n=="u":
#     print("vowel")
# else:
#     print("Consonant")

# 19. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16

# l=int(input("Enter a number:"))
# m=int(input("Enter another number"))
# n=input("Enter operator:")
# if n=="+":
#     print(l+m)
# elif n=="-":
#     print(l-m)
# elif n=="*":
#     print(l*m)
# elif n=="/":
#     print(l/m)
# elif n=="%":
#     print(l%m)
# elif n=="//":
#     print(l//m)
# else:
#     print("wrong input or operator!!")


# for i in range(1,7):
#     print("python")
# print("learning python")
b="multiverse"
for i in b:
    print(i)
