#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Find_score(Candidate_response,answer):
    Candidate_response = Candidate_response.lower()
    answer = answer.lower()
    max_score = 0
    cad_score = 0
    points = { 1:4, 2:3, 3:0, 4:1}
    r = Candidate_response.split()
    a = answer.split()
    for i in range(0,len(a)):
        po = 0
        size = len(a[i])
        if(a[i].isnumeric()):
            po = points[1]
        elif(len(a[i])>7):
            po = points[2]
        elif(len(a[i])<5):
            po = points[3]
        else:
            po = points[4]
        max_score = max_score + po
        if(i<len(r)):
            if(r[i] in a):
                cad_score = cad_score + po
    print(f"Candidate Score is : {cad_score}")
    print(f"Maximum Score is : {max_score}")
    if(max_score==0):
        return 100
    if(cad_score==0):
        return 0
    per = (cad_score/max_score)*100
    return per

cad_res = input("Enter the Candidate_response : ")  
corct_ans = input("Enter the Answer : ")  
score ="{:.2f}".format(Find_score(cad_res,corct_ans))
print(f"Percentage of Candidate : {score}")


# In[ ]:




