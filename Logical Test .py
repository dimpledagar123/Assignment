#!/usr/bin/env python
# coding: utf-8

# In[1]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz: "+str(num))
    elif num % 3 == 0:
        print("Fizz:" +str(num))
    elif num % 5 == 0:
        print("Buzz:" +str(num))
    else:
        print(num)


# In[ ]:




