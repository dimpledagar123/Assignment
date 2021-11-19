#!/usr/bin/env python
# coding: utf-8

# Write a Python program to reverse a string.
# 
# 
# 
# ﻿Sample String : "1234abcd"
# 
# Expected Output : "dcba4321"

# In[2]:


def reverse (string):
    reversed_string = ""
    for i in string:
        reversed_string = i+reversed_string
    print("reversed string is:",reversed_string)

string = input("enter a string:")
print("entered string",string) 
reverse(string)

