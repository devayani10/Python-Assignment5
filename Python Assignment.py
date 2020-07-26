#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [0,1,2,10,4,1,56,2,0,1,3,0,54,0,4]
list1.sort()
print(list1)
"LEFT ROTATION"
list1=list1[4:]+list1[0:4]
print(list1)


# In[6]:


def merge(list1, list2): 
    sorted_list = [(list1[i], list2[i])for i in range(0, len(list1))] 
    return sorted_list 
list1 = [10,20,40,60,70,80] 
list2 = [5,15,25,35,45,60] 
print(merge(list1, list2)) 


# In[ ]:




