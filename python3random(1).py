# 1)revserse string -> write a python to reverse a string without any buit in methods like reverse() or slicing
def reverse(string):
    temp=''
    for char in string:
        temp = char + temp
    return temp

try:
    word=input('enter the word:')
    print('original word:',word )
    print('reversed word:',reverse(word))
except ValueError:
    print('enter string only')


# 2)palindrome -> function to check if a given a string is a palindrome or not.
def check_palin(string):

    temp_word= ''.join(char for char in string if char.isalnum())
    reverse_word= temp_word[::-1]

    return 'palindrome' if temp_word == reverse_word else 'not palindrome'

try:
    word= input('enter word:')
    print('your word',word,'is',check_palin(word.lower()))
except ValueError:
    print('enter only string')


# 3)factorial -> function to calculate the factorial of given number using recursion
def factorized(n):
    if n== 0:
        return True
    else:
        return n * factorized(n-1)

try:
    val=int(input('enter number:'))
    print('factorized answer:',factorized(val))
except Exception:
    print('string not allowed')


# 1)difference between == and is in python?
#-> The == operator in Python is used to compare two values are equals or not. On the other hand, the is operator is used to check whether two variables refer to the same object in memory.

# 2)what is generator in python?
#-> Generators in Python used to generate values lazily/slowly, meaning they generate/produce values one at a time and only when needed. it is memory-efficient.

# 3)what is list comprehensions give example?
#->  it is compact or small syntax for generating lists on existing iterable, like string, list etc.
