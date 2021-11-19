#!/usr/bin/env python
# coding: utf-8

# ite a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# 
# 
# ﻿Sample String : 'The quick Brow Fox'
# 
# Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[7]:


def string_test(s):
   d={"UPPER_CASE":0, "LOWER_CASE":0}
   for c in s:
       if c.isupper():
           d["UPPER_CASE"]+=1
       elif c.islower():
           d["LOWER_CASE"]+=1
       else:
           pass
   print(f"original string",s)
   print("number of upper case alphabets:", d["UPPER_CASE"])
   print("number of lower case alphabets:", d["LOWER_CASE"])
string_test('The quick Brow Fox')

