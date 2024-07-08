#1) Write a function that takes a string as input and returns the reverse of the string.
def reverse_Word(word):
    # way 1 - slicing
    reverse_string = word[::-1]
    return reverse_string

    # way 2 - for loop
    # reverse_string=''
    # for char in word:
    #     reverse_string = char + reverse_string
    # return reverse_string

    # way 3 - reverse method
    # reverse_string= reversed(word) # make object thing 
    # reverse_string = list(reverse_string) # for object convert to list
    # reverse_string = ''.join(reverse_string)
    # return reverse_string

# print(reverse_Word('hello'))


# 2)Write a function to remove duplicates from a list of integers while preserving the original order.
def remove_dup(numbers):
    seen=set()
    temp=[]

    for num in numbers:
        if num not in seen:
            seen.add(num)
            temp.append(num)
    return temp

myList=[1,4,2,1,5,3,2]
print(remove_dup(myList))


# 3)Write Python code to read a text file line by line and print each line with its line number.
def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1
              
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read file '{filename}'.")

filename = 'sample.txt'  # Replace with your file path
read_and_print_file(filename)


# 4) Define a class Rectangle with attributes width and height. Implement methods to calculate its area and perimeter.
class Rectangle():
    def __init__(self,width,height):
        self.wid=width
        self.hei=height

    def area(self):
        return self.wid * self.hei
    
    def perimeter(self):
        return 2 * (self.wid * self.hei)
    
rect1=Rectangle(5,2)
print(rect1.area()) # o/p -> 10
print(rect1.perimeter()) # o/p -> 20


#5)Write a function that takes two integers as input and performs division. Handle the ZeroDivisionError exception if the second integer is zero.
def division(val1, val2):
    try:
        final = val1 / val2
        print(f"Division result: {final}")
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')

try:
    val1 = int(input('Enter value 1: '))
    val2 = int(input('Enter value 2: '))
    divisio(val1, val2)
except ValueError:
    print('Error: Please enter valid integers.')


# 6) Write a Python program to count the frequency of words in a given text file and store them in a dictionary.
def count_word(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            counter = {}

            for word in words:
                counter[word] = counter.get(word, 0) + 1

            return counter

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        return {}

filename = 'sample.txt'  # Replace with your file path
word_counts = count_word(filename)
print(word_counts).


#7)Write a recursive function to compute the factorial of a non-negative integer.
def fact_check(n):
    if n < 0:
        return 'value must be positive'
    
    if n == 0:
        return 1
    else:
        return n * fact_check(n - 1)
    
print(fact_check(5))


# 8)Implement a simple example using Python's threading module to demonstrate concurrent execution of two functions.
import threading

def counter(num):
    while num > 0:
        print(num)
        num -= 1

t1=threading.Thread(target=counter,args=(10,))
t2=threading.Thread(target=counter,args=(10,))

t1.start()
t2.start()
t1.join()
t2.join()
