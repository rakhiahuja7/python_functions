#question 1
a=input("enter first digit of number")
b=input("enter second digit of number")
def palindrome(a,b):
    if a+b==b+a:
        print("number is palindrome")
    else:
        print("number is not palindrome")
palindrome(a,b)
#question 2
def calculator():
    num1=float(input("enter first number"))
    num2=float(input('enter second number'))
    print('enter from these options when asked for operation add for addition,substract for substraction, multiply for multiplication and divide for division')
    operation=input('enter operation to be performed')
    if operation=='add':
        print(num1+num2)
    elif operation=='substract':
        print(num1-num2)
    elif operation=='multiply':
        print(num1*num2)
    elif operation=='divide':
        print(num1/num2)
    else:
        print('invalid choice')
calculator()

#question 3  
def counter():
    s=input("enter a word")
    for i in s:
        print(i,end=" ")
        print('-->',end=' ')
        print(s.count(i))

counter()
#question 4
def right_angle_triangle():
    n=int((input('enter number of rows')))
    i=1
    for i in range(i,n+1,1):
        print('*'*i)
    

right_angle_triangle()
#question 5      
def multiplication_table():
    n=int(input('enter a number for its table'))
    for i in range(11):
        print(n,end='')
        print('*',end='')
        print(i,end='')
        print('=',end='')
        print(n*i)

multiplication_table()
    