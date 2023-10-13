#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set
s= {}
print(s)
print(type(s))


# In[2]:


s= {1,2,3,4}
print(s)
print(type(s))


# In[8]:


s =([50,60,70])
print(s)
print(type(s))


# In[7]:


s[0]


# In[9]:


z = (20,30,40)
print(z)
print(type(z))


# In[10]:


tuple3 = tuple((1, 3, 5, "hello"))
print(tuple3)


# In[11]:


set1 = {1, 2, 3, 'abc', 6}
print(set1)


# In[13]:


l = [20,30,40]
print(l)
print(type(l))


# In[14]:


t = tuple(l)
print(t)


# In[17]:


#  Important function of set
# 1.  add(x)
# add item x to set



# In[26]:


s ={50,60,70}
print(s)
print(type(s))


# In[28]:


s.add("Rahul")


# In[29]:


print(s)


# In[4]:


### 2. update (x,y,z)\n",
    # To add multiple items to the set\n",
    # It should be either in list or in range\n",
     
        


# In[5]:


s1 = {10,20,30,40}
print(s1)


# In[6]:


l = [90,80,70,60,50,40]
print(l)


# In[7]:


s1.update(l)
print(s1)


# In[10]:


s2 = {"rahul", "sonali"}
s1.update(s2)
print(s1)


# In[8]:


# copy()
# cloning


# In[9]:


p =s1.copy()
print(p)


# In[11]:


# pop()  set does not follow order. It will remove randomly
s1.pop()
s1


# In[12]:


s1.pop()


# In[13]:


s1


# In[19]:


# remove() it removes specify element from the set

s = {90,80,70,60}
s.remove(70)
print(s)
s.remove(100)


# In[15]:


t = {6,4,2,2,9}
print(t)


# In[16]:


rm = [6,9]
r = t -set(rm)
r


# In[18]:


# discard - it remove specified item

s = {90,80,70,60}
s.discard(70)
print(s)
s.discard(100)


# In[20]:


# clear()  to remove all element
s ={10,20,30,40}
print(s)


# In[22]:


s.clear()
s


# In[23]:


# ##### Mathematical Operations on Set ---\n",
    ###  1. union() ### x.union(y) or x|y\n",
    ### we can use this function to return all elements present in both sets\n",
   


# In[28]:


x = {10,20,30}
y = {30,40,50}
print(x.union(y))
print(x|y)
    


# In[31]:


x = {10,20,30}
y = {30,40,50,"rahul"}
z= x.union(y)
print(z)


# In[29]:


#### 2. Intersection\n",
    ### x.intersection(y) or x&y\n",
    ### RReturns common element present in both x and y\n",


# In[32]:


x.intersection(y)


# In[34]:


#### 3. Difference\n",
    #### x.differeence(y) or x -y\n",
    ##### returns the element present in x but not in y\n",
x = {10,20,30,40}
y = {30,40,50,60}
print(x.difference(y))
print(y.difference(x))


# In[35]:


####4. Symmetric Difference\n",
#### x.symmetric_difference(y) or x^y\n",
#### returns element present in either x or y but not in both\n",
x = {10,20,30,40}
y = {30,40,50,60}
print(x.symmetric_difference(y))


# In[36]:


#### Membership Operators in Set (in and not in)\n",
s = set("Sonali")  ##### Another way of Tokenizing of words\n",
print(s)


# In[37]:


print('i' in s)


# In[39]:


print('k' not in s)


# In[40]:


s1.difference_update()


# In[ ]:


##### Dictionary Data Structure\n",
#### we can use listm tuple, set to represent group mof individual objects \n",
###if you want to create group of obejcts as key and value pairs then we should go for dict\n",
# name - \"Sonali\"\n",
# age - 27\n",
#\n",
#### Dupliate keys are not allowed but values can be duplicated\n",
#### Hetrogenous objects are allowed for both key and value\n",
#### Insertion order is not preserved\n",
#### Dictionaries are Mutable objects\n",
### Dictionaries are Dynamic\n",
##### Indexing and slicing are not applicable"


# In[41]:


d = {}
print(d)
print(type(d))


# In[42]:


d  = {1 : 'rahul', 2: 'Rohan', 3:'sheetal'}
print(d)


# In[43]:


d[1]


# In[44]:


d[4]= "Abhishek"


# In[45]:


d


# In[46]:


d[9]


# In[47]:


del d[4]


# In[48]:


d


# In[49]:


d[5] = "Anand"


# In[50]:


d


# In[51]:


s = {23 : 'ABC', 89: 'DEF'}
s


# In[52]:


d.update(s)
d


# In[53]:


n = {'name':['Rahul', "Rohan", "Sita"], 'Age':[12,25,26]}
print(n)


# In[54]:


n.clear()
print(n)


# In[55]:


d.keys()


# In[56]:


d.values()


# In[58]:


d.items()


# In[60]:


d.pop(2)


# In[61]:


d


# In[62]:


d.popitem()


# In[63]:


d


# In[64]:


e = d.copy()


# In[65]:


e


# In[66]:


#### Range - We can create range of values - \n",
list(range(5))


# In[67]:


list(range(1,25,2))


# In[68]:


##### None nothing No values are associated\n",
### if the value isw not available, then to handle such type of cases None are introduced.\n",
a = None
print(a)


# In[69]:


##### Escape Characters\n",
### \\n == New Line\n",
print("Rahul is a good boy, he plays very well")
#### \\t  == Horizontal Tab\n",
print("Rahul is a good boy he plays very well")


# In[71]:


### Operators in Python\n",
### 1. Arithmetic Operators\n",
    #### + , - , * , / , %, // , **\n",
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)   ### Reminder \n",
print(a//b)   ##### Floor\n",
print(a**b)


# In[72]:


#### In string there are 2 operator + and *


# In[73]:


#### Relational Operators (>, >= , < ,<=)\n",
a = 10
b = 20
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


# In[ ]:


#### Bool Data TYpe\n",
#### True and False


# In[74]:


#### In Python True represents as 1 and False represents as 0\n",
a = True
b = True
print(a+b)


# In[75]:


print(True > True)


# In[76]:


print(True >= True)


# In[77]:


print(0 > True)


# In[78]:


print(True != True)


# In[79]:


#Logical operators and , or , not


# In[80]:


# and  =  if both arguments are True then the results are True\n",
# or = if atleast one argument is True then result is True\n",
# not  = complement


# In[81]:


True and True


# In[82]:


True or False


# In[83]:


not True


# In[84]:


### if the 1st argumen tis 0, then the rsult is zero other wise the result i y\n",
10 and 20


# In[85]:


0 and 20


# In[86]:


#### x or y\n",
### if x is true then the result is x other wise result is y\n",
10 or 20


# In[87]:


0 or 20


# In[88]:


##### Modules in Python  - Modules are bascially packages which stores differnt dunctions related\n",
#### to that module\n",
#### import module_name\n",
#### from module_name import functions\n",
#### import module_name as alias


# In[89]:


import math as m


# In[90]:


m.sqrt(4)


# In[91]:


m.pi


# In[92]:


from math import sqrt,pi


# In[93]:


sqrt(16)


# In[94]:


pi


# In[95]:


import datetime


# In[96]:


k = datetime.date(1996,12,11)
print(k)
print(type(k))


# In[97]:


t = datetime.date.today()
print(t)


# In[100]:


print("Current Year",t.year)
print("Current Month",t.month)
print("Current Day ",t.day)


# In[104]:


from datetime import time


# In[105]:


t = time(11,34,56)
print(t)


# In[107]:


print("Hour", t.hour)
print("Minutes", t.minute)
print("Seconds", t.second)


# In[ ]:


#### Write a program taking input from user and calculate the area of a circle


# In[108]:


### pi r sqaure  ##### \n",
radius = int(input("Enter the Radius"))
aoc = pi*(radius**2)
print(aoc)


# In[ ]:




