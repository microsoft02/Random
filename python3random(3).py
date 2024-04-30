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
