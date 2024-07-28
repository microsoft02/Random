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
    # or
    #  reverse_string = ''.join(reverse_string)
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


#9) arrange the list l1=[6,9,3,1] decline l1=[9,6,3,1] without using any built it method (probably need to create custom function)(bit confusing but go stepwise) 
def rearrange(myList):
  # first check if there only 1 or less than 1 element in list? if then return
  if len(myList) <= 1:
    return myList
  else:
    for i in range(len(myList)):                                 #mean range(0(default,4(list length)) so it will go index 0,1,2,3
      max_ind = i                                                # so at first we store 0 ind as max ind
      for j in range(i+1,len(myList)):                           # and here we adding 1 in i mean 0+1, 4(list length)
        if myList[j] > myList[i]:                                #then here mylist[1] greater than myList[0] -> 9 > 6 -> true # like this inner loop continue until range 1,2,3 time and compare the value
          max_ind = j                                            # so we store max_ind = 1    
      myList[i],myList[max_ind] =  myList[max_ind],myList[i]     # then we swap as mylist[0] ,myList[1]  =  myList[1], myList[0] -> mean  [6],[9] = [9], [6]
  return myList                                                  # finally we return it's outside loop 

l1=[6,9,3,1]
rearrange(l1)


#10)merge two dict dict1 = {'a': 1, 'b': 2, 'c': 3} and dict2 = {'b': 3, 'c': 4, 'd': 5} and get ans dict3 = {'a': 1, 'b': 5, 'c': 7, 'd': 5}. only this method is bit simple.
def mergeing_dicts(dict1, dict2):
    result = dict(dict1)         # Start with a copy of dict1  for match with dict2 items
    for k, v in dict2.items():   # for dict you can or you have to use two varaible if want to make key and value seperate inside variable, dict2.items() -> items return the dict element with key and value in tuple and this tuple are inside list
        result[k] = result.get(k, 0) + v   # result have all dict1 key and vlaue so in k we have stored only key name so result[k] mean a <- which was in dict1 a = result.get(a,0(default)) + v , get method you have to pass the key which is a
                                          # and v is the value from dict2 it will get add in value of dict1. loop will repeat until all dict done
    return result                  # then retun result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

dict3 = mergeing_dicts(dict1, dict2) # send both dict in function

print(dict3)

  # way2 there other way some built in thing called collections it have counter which count the lement how many time it occurance here how and counter give dict in tuple dict keys are in descending order.

from collections import Counter
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
                                                #also you can not concat two dict therefore counter good they count and convert into tuple you can concate tuple.
dict3 = dict(Counter(dict1) + Counter(dict2))  #-> counter will give answer like this for dict1 -> ({'c':3,'b':2,'a':1})  and due it's return tuple we convert it to dict using dict

print(dict3)
