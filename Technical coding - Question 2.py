#!/usr/bin/env python
# coding: utf-8
# Python Candidates -



﻿Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the

comments of the code. Also you will have to print the following after validation in respective functions:-

1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

2.Valid Triangle:If the triangle sum property of sides is valid.

3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

4.Invalid Rectangle: If Not Valid rectangle as stated above.

Input Format:

The side length of triangle followed by for rectangle in the next line in order.

Output Format:

since object are created in order, so first validate info about triangle will come and than rectangle.

Sample Input 0:

3 4 5

2 4 2 4

Sample Output 0:

Valid Triangle

Valid Rectangle


# In[2]:


class Triangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_triangle(self,l):
        if len(l)==3 and (l[0]+l[1])>l[2]:
            return "Valid Triangle"         
        else:
            return "Invalid Triangle"
class Rectangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_rectangle(self,l):
        if len(l)==4 and  (l[0]==l[2]) and (l[1]==l[3]):
            return "Valid Rectangle"         
        else:
            return "Invalid Rectangle"
T=list(map(int,input().split()))
R=list(map(int,input().split()))
A=Triangle(T)       
print(A.validate_triangle(T))
B=Rectangle(R)
print(B.validate_rectangle(R))


# In[ ]:




