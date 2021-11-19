#!/usr/bin/env python
# coding: utf-8

#  Write a Python function to sum all the numbers in a list.
# 
# 
# 
# Sample List : (8, 2, 3, 0, 7)
# 
# Expected Output : 20
# 
# 
# 
# Explanation:
# 
# 
# 
# Summation should like 8+2+3+0+7 = 20

# In[8]:


def add_multiple_numbers(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

numbers = (8, 2, 3, 0, 7)
sum_of_multiple=add_multiple_numbers(8, 2, 3, 0, 7)
print(sum_of_multiple)


# In[ ]:




