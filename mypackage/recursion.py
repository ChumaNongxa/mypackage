def sum_array(array):
    '''Return sum of all items in array'''
    if len(array)==1:
        return array[0]
    elif len(array) >1:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n<=1:
        return n
    elif n>1:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''Return n!'''
    if n==0:
        return 1
    if n==1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    '''Return word in reverse'''
    word_len = len(word)
    if word_len ==1:
        return word
    elif word_len>1:
        return reverse(word[1:]) + word[0]
