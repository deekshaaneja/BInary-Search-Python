
# coding: utf-8

# In[3]:


def binary_search(array, value):
    index = int(len(array)/2) -1
    end = int(len(array)) - 1
    while array[index] != value:
        if index == end:
            return -1
        elif array[index] > value:
            end = index
            index = int(index/2)
        elif array[index] < value:
            index = int((index+1 + end)/2)
    return index
binary_search([1,3,9,11,15,19,29], 19)

