#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Declare a string and store it in a variable. 

#Check the type and print the id of the same.

str1 = "This is a Python Class"

print(type(str1))
print(id(str1))


# In[ ]:


#Which are valid/invalid strings
1. 'This is Python class' :  Valid
valid/invalid

2. "This is Python class" :  Valid
valid/invalid

3. '''This is Python class''' :  Valid
valid/invalid

4. """This is Python class""" :  Valid
valid/invalid

5. 'This is Python's class'  :  InValid
valid/invalid

6. "Learnbay provides "Java", "Python" classes" :  InValid
valid/invalid

7. "Learnbay provides 'Java', 'Python' classes" :  Valid
valid/invalid

8. "This is Python's class" :  Valid
valid/invalid

9. """Learnbay provides "Java", "Python" classes""" :  Valid
valid/invalid

10. '''Learnbay provides "Java", "Python" classes''' :  Valid
valid/invalid   #

11. '''Learnbay provides
"Java", "Python" 
classes'''
valid/invalid :  Valid

12. 'This is
Python 
class'
valid/invalid :  InValid


# In[18]:


#Write the code to get the output mentioned below print statement
my_str = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."

print(f"The length of my_str is {len(my_str)}")
#output:- The length of my_str is 66

print(id(my_str) == id(my_str1))
#output:- id of my_str and my_str1 is same? - True

print(f"Type of my_str is: {type(my_str)}")
#output:- Type of my_str is: str


# In[29]:


#Indexing
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
#Write the code to get the output,instructions are mentioned below print statement. use indexing

print(f"The first character in my_str is: {my_str[0]}")
#output:- The first character in my_str is: A
#Note:- Use positive indexing

print(f"The first character in my_str is: {my_str[len(my_str)-1]}")
#output:- The first character in my_str is: h
#Note:- Use len() function.

print(f"The character at index 10 in my_str is: {my_str[9]}")
#output:- The character at index 10 in my_str is: c
#Note:- Use positive indexing

print(f"The last character in my_str is: {my_str[-1]}")
#output:- The last character in my_str is: h
#Note:- Use negative indexing.

print(f"The last character in my_str is: {my_str[len(my_str)-1]}")
#output:- The last character in my_str is: h
#Note:- Use len() function.

print(f"The character in my_str is: {my_str[9]}")
#output:- The character in my_str is: 8
#Note:- Use positive index


# In[88]:



#Slicing
my_str = "Although that way may not be obvious at first unless you're Dutch."
#Write the code to get the output,instructions are mentioned below print statement. use slicing
print(f"You have sliced: {my_str[::]}")
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.Without begin, end and step


print(f"You have sliced: {my_str[0:len(my_str):]}")
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.with begin as 0 end using len and without step


print(f"You have sliced: {my_str[::1]}")
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.without begin and end but using step


print(f"You have sliced: {my_str[0:len(my_str):1]}")
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.With begin, end and step


print(f"You have sliced: {my_str[len(my_str):len(my_str):-1]}")
#output:- You have sliced:   .with using begin and end using postive values and step as negative values.
#Slicing command should print empty string.


print(f"You have sliced: {my_str[0:len(my_str):2]}")
#output:- You have sliced: Atog htwymyntb biu tfrtuls o'eDth


print(f"You have sliced: {my_str[0:len(my_str):3]}")
#output:- You have sliced: Ahgttam tebo  r lsorDc


print(f"You have sliced: {my_str[::-1]}")
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use only step


print(f"You have sliced: {my_str[len(my_str)::-1]}")
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use begin end and step.
# Doubt : how to print the last element with end as 0 and -1 as step during slicing

print(f"You have sliced: {my_str[::-2]}")
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use only step


print(f"You have sliced: {my_str[len(my_str)::-2]}")
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use begin, end and step.


print(my_str[10:17:-1])
#What will be the output?  ## space


print(f"You have sliced:{my_str[17:10:-1]}")
#output:- You have sliced: yaw ta, Using begin, end and step.

print(f"You have sliced:{my_str[49:56:1]}")
#output:- You have sliced: ess you. Using begin, end and step.


# In[8]:


#Basic operation on string
str1 = 'Learnbay'
str2 = 'Python'

#Write the code to get the output,instructions are mentioned below.
#Output is: Learnbay Python
print(str1 + " " +str2)

# print(str1 + " " +1.0)


#Error: TypeError: can only concatenate str (not "int") to str


#Error: TypeError: can only concatenate str (not "float") to str



#Find below Output
#Output is: LearnbayLearnbayLearnbay
print(str1*3)
# print(str1*3.0)
# print(str1*str2)


#Error: TypeError: can't multiply sequence by non-int of type 'float'


#Error: TypeError: can't multiply sequence by non-int of type 'str'


# In[17]:


#Find below Output
str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

#print True by using identity operator between str1 and str2
print(str1 is str2)


#print False by using identity operator between str1 and str3
print(str1 is str3)


#print False by using identity operator between str4 and str3
print(str3 is str4)


#Check if P is available in str1 and print True by using membership operator
print('P' in str1)


#Check if $ is available in str3 and print True by using membership operator
print('$' in str3)


#Check if N is available in str3 and print False by using membership operator
print('N' in str3)



# In[20]:


#Complete the below code
str1 = 'This is Python class'
#write the code to replace 'Python' with 'Java' and you should get below error.
#TypeError: 'str' object does not support item assignment.
str1.replace('Python','Java')
# str1[9]=J



# In[28]:


str1 = 'A'
str2 = 'A'
#Compare str1 and str2 and print True using comparison operator
print(str1 is str2)


#Compare str1 and str2 and print True using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 is not str2)


# In[32]:


str1 = 'A'
str2 = 'a'
#Compare str1 and str2 and print True using comparison operator
print(str1 is not str2)


#Compare str1 and str2 and print True using equality operator
print(str1 != str2)


#Compare str1 and str2 and print False using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 is str2)


# In[54]:


str1 = 'A'
str2 = '65'
#Compare str1 and str2 using comparison operator and it should give below error.
#Error: TypeError: '>=' not supported between instances of 'str' and 'int'
# print(str1 >= int(str2))
print(str1 >= str2)


#Compare str1 and str2 and print True using equality operator
print(ord(str1)== int(str2))

#Compare str1 and str2 and print False using equality operator
print(ord(str1)== str2)


# In[58]:


str1 = 'Python'
str2 = 'Python'
#Compare str1 and str2 and print True using comparison operator
print(str1 is str2)

#Compare str1 and str2 and print True using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 is not str2)


# In[60]:


str1 = 'Python'
str2 = 'python'
#Compare str1 and str2 and print True using comparison operator
print(str1 is not str2)

#Compare str1 and str2 and print True using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 is str2)


# In[69]:


a = 'Python'
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a and b)
print(a or b)
print(not(a == b))
print(not(a or b))
print(not(a and b))


# In[70]:


a = ''
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a and b)
print(a or b)
print(not(a == b))
print(not(a or b))
print(not(a and b))


# In[71]:


a = 'Python'
b = 'learnbay'

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a and b)
print(a or b)
print(not(a == b))
print(not(a or b))


# In[3]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to get the total count of 't' in above string. Use find() and index() method.
print(my_str.count("t"))
print(my_str.find("t",0,20))
print(my_str.index("t"))

#Write the code to get the index of '8' in my_str. Use find() and index() method.
print(my_str.index("8"))
print(my_str.find("8"))

#What will be the output of below code?
print(my_str.find('the'))


# print(my_str.index('the'))


print(my_str.find('t', 9, 15))


print(my_str.rfind('u'))


print(my_str.rindex('u'))


# In[7]:


#W A P which applies strip() method if any string, which will be taken from user, starts and ends with space, or applies 
#rrstrip() method if that string only ends with space or applies lstrip() method if that string only starts with a space.

#For example:-
#input:- '    Python   '
#output:- 'Python'

my_str = '    Python   '
my_str.rstrip().lstrip()

#input:- '    Python'
#output:- 'Python'
my_str = '    Python'
my_str.lstrip()

#input:- 'Python   '
#output:- 'Python'
my_str = 'Python   '
my_str.rstrip()


# In[10]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to convert all alphabets in my_str into upper case.
print(my_str.upper())

#Write the code to convert all alphabets in my_str into lower case.
print(my_str.lower())

#Write the code to swap the cases of all alphabets in my_str.(lower to upper and upper to lower)
print(my_str.swapcase())


# In[13]:


#Write the code which takes one string from user and if it starts with small case letter then convert it to corresponding 
#capital letter otherwise if starts with capital letters then convert first character of every word in that string into capital.

my_str = input("Enter the string: ")

if my_str[0].islower():
    print(my_str.capitalize())
else:
    print(my_str.title())


# In[32]:


#Take a string from user and check if it is:-
#     1. alphanumeric
#     2. alphabets
#     3. digit
#     4. all letters are in lower case
#     5. all letters are in upper case
#     6. in title case
#     7. a space character
#     8. numeric
#     9. all number elements in string are decimal

my_str = input("Enter the string: ")

if my_str.isspace():
    print("The string is a space cahracter.")
elif my_str.isnumeric():
    print("The string is a numeric.")
elif my_str.isdecimal():
    print("The string is a decimal.")
elif my_str.isdigit():
    print("The string is a decimal.")
elif my_str.istitle():
    print("The string is a Titelcase.")
elif my_str.isalpha():
    print("The string is a Alphabetic.")
elif my_str.isalnum():
    print("The string is a Alphanumeric.")
elif my_str.islower():
    print("The string is a lowercase string.")
elif my_str.isupper():
    print("The string is a uppercase string.")
else:
    print("None of these")
    


# In[4]:


#W A P which takes a string as an input and prints True if the string is valid identifier else returns False.
#Sample Input:- 'abc', 'abc1', 'ab1c', '1abc', 'abc$', '_abc', 'if'

my_str = input("Enter the string: ")

my_str.isidentifier()



# In[8]:


#What will be output of below code?
s = chr(65) + chr(97)
print(s.isprintable())

s = chr(27) + chr(97)
print(s.isprintable())

s = '\n'
print(s.isprintable())

s = ''
print(s.isprintable())


# In[14]:


#What will be output of below code?
my_string = '  '
print(my_string.isascii())

my_string = 'Studytonight'
print(my_string.isascii())

my_string = 'Study tonight'
print(my_string.isascii())

my_string = 'Studytonight@123'
print(my_string.isascii())

my_string = '°'
print(my_string.isascii())

my_string = 'ö'
print(my_string.isascii())


# In[15]:


#What will be the output of below code?
firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')


# In[19]:


#Write the code to get below output
#O/P 1:- python** (using ljust method)
my_str = "python"

my_str.ljust(8,'*')

#Write the code to get below output
#O/P 1:- **python (using rjust method)
my_str.rjust(8,'*')


#Write the code to get below output
#O/P 1:- **python** (using rjust method)
my_str.ljust(8,'*').rjust(10,'*')


# In[20]:


#Write a Python program to find the length of the my_str:-

#Input:- 'Write a Python program to find the length of the my_str'
#Output:- 55
my_str ='Write a Python program to find the length of the my_str'
len(my_str)


# In[21]:


#Write a Python program to find the total number of times letter 'p' is appeared in the below string:-
    
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 9
my_str ='peter piper picked a peck of pickled peppers.'

my_str.count('p')


# In[ ]:


#Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string:-
    
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers. pickled of peck a picked piper peter'


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers.'


# In[ ]:


#Write a python program to find below output:-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
#Output:- 'Peter piper picked a peck of pickled peppers.'


# In[ ]:


#Write a python program to implement index method. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
#Output:- 29


# In[ ]:


#Write a python program to implement replace method. If sub_str is found in my_str then it will replace the first 
#occurrence of sub_str with new_str else it will will print sub_str not found:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'


# In[ ]:


#Write a python program to find below output (implements rjust and ljust):-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
#Output:- '*********************Peck********************'



# In[ ]:





# In[ ]:




