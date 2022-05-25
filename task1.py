#1 .. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

# a=int(input("Enter your desired number: "))
# b=int(input("Enter your other number: "))
# if a==b:
#     print("1")
# elif a>b:
#     print("2")
# else:
#     print("3")

#________________________________________________________________________________

#2. Print "Hello" if a is equal to b, and c is equal to d.  
# a=int(input("Enter number A: "))
# b=int(input("Enter number B: "))
# c=int(input("Enter number C: "))
# d=int(input("Enter number D: "))
# if a==b and c==d:
#     print("HELLO")
# else:
#     print("Nice to meet you! ")

#_______________________________________________________________
 
#3. Print "Hello" if a is equal to b, or if c is equal to d.

# a=int(input("Enter number A: "))
# b=int(input("Enter number B: "))
# c=int(input("Enter number C: "))
# d=int(input("Enter number D: "))
# if a==b or c==d:
#     print("HELLO")
# else:
#     print("Nice to meet you! ")
#_______________________________________________________________---

#4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

# x=int(input("Enter an integer: "))
# if x>0:
#     print("True")
# elif x<0:
#     print("False")
# else:
#     print("Zero")

#_____________________________________________

# 5. Check whether the user input number is even or odd and display it to user.
# c=int(input("ENTER A NUMBER: "))
# if (c%2==0):
#     print("Even")
# else:
#     print("Odd")

#________________________________

#6.  WAP which accepts marks of four subjects and display total marks, percentage and grade.
g=int(input("Enter maths mark; "))
h=int(input("Enter your programming mark;"))
i=int(input("Enter your software design mark; "))
j=int(input("Enter your algo marks; "))
x=g+h+i+j
print(x)
y=x/400*100
print(y)
if y>70:
    print("Distinction")
elif y>60:
    print("First Division")
elif y>40:
    print("Pass")
else:
    print("Fail")
#_________________________________________________

#7. What is the output of ‘APPLE’ > ‘apple’?
 #false

#8. Write a Python program to display your details like name, age, address in three different lines.

# def personal_details():
#     name, age = "Pramesh", 20
#     address = "167 K.U.K.L-Jay Ganesh Galli-16,Parijat sadak,44600-Kathmandu"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
 
# personal_details()

#_______________________________________________________

#9. Write a python program which accepts the radius of circle from user and compute the area.

# r=float(input("ENTER THE RADIUS OF THE CIRCLE FOR FINDING OUT ITS AREA; "))
# pi=22/7
# a=pi*r**2
# print(a)
#__________________________________________________________________


#10. A school decided to replace the desks in three classrooms. Each desk sits two students. 
# Given the number of students in each class, print the smallest possible number of desks 
# that can be purchased.

# The program should read three integers: the number of students in each of the three 
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 
# desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total. 

# a=int(input("Enter the number of students in first class; "))
# b=int(input("Enter the number of students in second class; "))
# c=int(input("Enter the number of students in second class;"))
# d=(a+b+c)/2
# print(d,"are the required number of total desks.")

#______________________________________________________________________-

#11. Given three integers, print the smallest one. (Three integers should be user input)

# a = int(input("Enter first number  : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number  : "))
# smallest = 0
# if a < b and a < c :
#     smallest = a
# if b < a and b < c :
#     smallest = b
# if c < a and c < b :
#     smallest = c

# print(smallest, "is the smallest of three numbers.")

#_________________________________________________________________________________-

#12. Write a program that takes three numbers and prints their sum. Every number is given on 
# a separate line.

# a=int(input("Enter 1st number; "))
# b=int(input("Enter 2nd number; "))
# c=int(input("Enter 3rd number; "))
# d=(a+b+c)
# print(a)
# print(b)
# print(c)
# print(d,"is the sum of three numbers")

#___________________________________________________

# 13. Write a program that reads the length of the base and the height of a right-angled triangle 
# and prints the area. Every number is given on a separate line.

# b=float(input("Enter the length of the base of a right angled triangle; "))
# h=float(input("Enter the length of the height of a right angled triangle; "))
# A=(b*h)/2
# print(b)
# print(h)
# print(A,"is the area of the given RA triangle")

#_____________________________________________________________________________

# 14. N students take K apples and distribute them among each other evenly. The remaining 
# (the undivisible) part remains in the basket. How many apples will each single student 
# get? How many apples will remain in the basket? The program reads the numbers N and 
# K. It should print the two answers for the questions above.


# n=int(input("Enter number of student; "))
# k=int(input("Enter number of apples; "))
# v=n//k
# h=n%k
# print(v,";is the number of apples shared each")
# print(h,";is the number of apple left over")


