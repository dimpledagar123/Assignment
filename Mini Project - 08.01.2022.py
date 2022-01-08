#!/usr/bin/env python
# coding: utf-8

# 1.) Regex Query Tool - A tool that allows the user to enter a text string and then in a separate control enter a regex pattern. It will run the regular expression against the source text and return any matches or flag errors in the regular expression.

# In[30]:


REGX = 'apple[A-Z0-9][a-z0-9]'
collection_of_strings = ['apple44DkiwiAE',
                         'apple55bananas',
                        'apple6ckiwi',
                        'appleF7kiwi',
                        'applDakii',
                        'apple00kiwi',
                        'pple17kiwi']
for string in collection_of_strings:
    print(string,'-->',re.search(REGX, string))        


# In[ ]:




