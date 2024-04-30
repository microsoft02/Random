#1)Write a Python function to check if a given string is a palindrome or not.
def palin_check(string):
    # cleaning
    clean_word= ''.join(char for char in string if char.isalnum())

    # reverse way 1 - with slicing
    reverse_word= clean_word[::-1]

    #reverse way 2 - with for loop
    # reverse_word=''
    # for char in clean_word:
    #     reverse_word = char + reverse_word
    
    #reverse way 3 - with revserse method
    # reverse_word= reversed(clean_word)

    return 'it palindrome' if reverse_word == clean_word else 'is not palindrome'

word=input('enter word:')
print(palin_check(word))


#2) Create a Python program to find the factorial of a number using recursion.
def check_fact(n):
    if n==0:
        return 1   #factorial of 0 must 1 (maybe)
    else:
        return n * check_fact(n-1)

num=int(input('enter number:'))
print(num, 'the factorial answer:',check_fact(num))


#3) Implement a Python class called BankAccount with methods deposit() and withdraw() to manage a simple bank account.
class BankAccount():
    def __init__(self,bal):
        self.bal=bal

    def deposit(self,amount):
        self.bal += amount

    def withdraw(self,amount):
        self.bal -= amount

    def check_bal(self):
        return self.bal
user1=BankAccount(5000)

user1.deposit(1000)
print('balance after deposit:',user1.check_bal())

user1.withdraw(500)
print('balance after withdraw:',user1.check_bal())


# 1) What is the difference between append() and extend() methods in Python lists?
# -> 'append()' use to insert single value at a time at the end of list. you can only give one value or parameter in this method.
temp_list = [1, 2, 3]
temp_list.append(4)
print(temp_list)  # Output: [1, 2, 3, 4]

# 'extend()' use to insert multiple value or can be single but it need iterable object which is tuple or list or other. it att value at the end of list.
temp_list = [1, 2, 3]
temp_list.extend([4, 5])
print(temp_list)  # Output: [1, 2, 3, 4, 5]


# 2) Explain the purpose of __init__ method in Python classes.
# -> __init__ use to initialize the instance of class object. it also called it constructor too. when new object created, python call the init function automatically
# and get the name and age of that user.

class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person1 = user("Alice", 10)

# Accessing attributes of the instance
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 10


# 3) How does Python's garbage collection mechanism work, and what are some ways to manage memory in Python programs?
# -> for garbage collection it deallocate the memory that is not in use. mean if there is no stored value then memory address get free (maybe) 
# Python uses a technique called reference counting combined with a cycle-detecting garbage collector to manage memory.

# for manage memory we can use generator that generate value when they actually need and called.
# and clost the files or folder completely that is not in use. so the extra memory will get free.
