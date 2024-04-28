# 1) Write a Python function to find the factorial of a number.
def factorized(n):
    if n==0:
        return True
    else:
        return n * factorized(n-1)

try:
    num=int(input('enter number:'))
    print(num, 'the factorized answer',factorized(num))
except ValueError:
    print('string not allowed')


# 2) Create a Python program to count the number of occurrences of each character in a given string.
def word_counter(string):
    # because we counting word so save 1) word and 2) count for this we need dictionary
    temp={}
    for char in string:
        # get method use in dict to get present key or new key must, value is optional so we can give the value here
        temp[char]=temp.get(char,0)+1
    return temp
try:
    word=input('enter word:')
    print(word_counter(word))
except ValueError:
    print('error')


# 3)Implement a Python class representing a simple bank account with methods to deposit, withdraw, and check balance.
class bank():
    def __init__(self,bal):
        self.bal=bal

    def deposit(self,amount):
        self.bal += amount

    def withdraw(self,amount):
        self.bal -= amount

    def check_bal(self):
        return self.bal
    
user1=bank(5000)

user1.deposit(1000)
print('after deposit',user1.bal)

user1.withdraw(500)
print('after withdraw',user1.bal)

print('your bal is:',user1.check_bal())


# 1)What is the difference between a list and a tuple in Python?
#-> list is collection of similar or different type of datatype, list is mutable mean the value/element can be change later. list is represent by square bracket []. 
# and tuple is same as list but tuple is im-mutable mean the value/element can't be change later. and tuple represent by round bracket ().

#2)How does Python manage memory?
#->Python manages memory using a private heap space. When you create a variable in Python, it's stored in memory along with its data. Python automatically handles memory allocation and deallocation through a mechanism called reference counting.

# 3)Explain the difference between == and is operators in Python.
# ->The '==' operator is used to check if the values of two variable/operands are equal.and the 'is' operator is used to check if two variables refer to the same object in memory i.e. if they have the same identity.
