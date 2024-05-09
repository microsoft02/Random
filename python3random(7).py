#1) Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list.
def evensum(numbers):
    total=0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return print('total of all even numbers:',total)

mylist=[3,5,2,1,4,7,6]
evensum(mylist)


#2) Create a Python class called Rectangle with attributes length and width. Include a method area() that calculates and returns the area of the rectangle.
class Rectangle():
    def __init__(self,length,width):
        self.len=length
        self.wid=width

    def cal_area(self):
        return self.len * self.wid

rect1=Rectangle(5,3)
print('the area of rectangle is:', rect1.cal_area())


#3) Write a Python program to find all prime numbers between 1 and a given number n.
def check_prime(n):
    if n <= 1:
        return print('it is non-prime number')

    for val in range(2,int(n ** 0.5)+1):
        if n % val:
            return print('it is not prime number')
    
    return print('it is prime number')

last_num=int(input('enter the value:'))
check_prime(last_num)


#1) Explain the concept of a Python generator. How is it different from a regular function?
#-> in python generator we use yield. it special iterator use over the iterable item but while keep program run continuous until. it store generated item 1 by 1 only in memory when they called.
# aside regular function generate all output and store all item in memory at once and chance to get memory full or slow down the system. 
def countdown(n):
    while n > 0:
        yield n
        n -= 1
      
for i in countdown(5):
    print(i)


#2) Explain the concept of a Python dictionary comprehensions. How do they differ from list comprehensions? Provide examples to illustrate their usage and syntax.
# Dictionary comprehensions in Python are similar to list comprehensions but are used to create dictionaries instead of lists.
# eg.
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#3) How does Python handle exceptions? Explain the try, except, else, and finally blocks in exception handling.
# -> in python exception handling done using try except block. try block were you write your code that you want find execption in that code.
# if the try block occure any exception it look in except block with exption type that match and then raise the error.
# else block is optional and is executed if no exceptions are raised in the try block. It's typically used to execute code that should run only if no exceptions occur.
# The finally block is optional and is always executed, regardless of whether an exception occurred in the try block.
try:
    pass
except ExceptionType:
    pass
else:
    pass
finally:
    pass
