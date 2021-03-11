#!/usr/bin/env python
# coding: utf-8

# In[13]:


a = 10
b = 5
try:
    c = a/b
except:
    print('Any number can not be divided by 0')
else:
    print(c)
finally:
    del(a)
    del(b)

print(c)


# In[25]:


my_inp = eval(input('Enter a dictionary: '))
key = eval(input('Enter a key: '))
try:
    print(my_inp[key])
except KeyError as k:
    print(k,'Sorry! this key is not there in the dictionary you have entered')
else:
    my_inp[key] = 'Class'
    print(my_inp)
finally:
    print('Excuting Finally')
    del my_inp, key


# In[28]:


type(eval('[12,22,44,12]'))


# In[32]:


import math
a = int(input('Enter 1st Number only integer: '))
try:
    b = int(input('Enter 2nd Number: '))
    e = eval(input('input a value: '))
    c = a/b
    d = a+e
    print(math.exp(10000))
    print(x)

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
except OverflowError as e:
    print(e)
except:
    print('Some Error')
else:
    print(c)
print(a)
print(b)


# In[42]:


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


# In[45]:


def Amount_Deposit(amt):
    if amt > 49999:
        raise MyException('Need Pan Card')
    else:
        print('Amount Deposited')

def submit_pan(pan):
    if len(pan) == 10:
        print('Thanks for sbmitting the PAN no, we will review your case')
    else:
        raise MyException('Wrong Pan No')


# In[46]:


try:
    Amount_Deposit(50000)
except MyException as e:
    print(e)
    try:
        pan = input('Enter your PAN: ')
        submit_pan(pan)
    except MyException as e:
        print(e)


# In[48]:


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
import random as rd
number = rd.randint(8,15)

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




