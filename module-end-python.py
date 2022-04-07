#!/usr/bin/env python
# coding: utf-8

# # module-end-python
# 
# Use the "Run" button to execute the code.

# In[ ]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[ ]:


import jovian


# In[ ]:


# Execute this to save new versions of the notebook
jovian.commit(project="module-end-python")


# In[8]:


#Q1


def convert_time (seconds):
    seconds=seconds%(24*3600)
    hour=seconds//3600
    seconds%=3600
    minutes=seconds//60
    seconds%=60
    return "%d:%02d:%02d" % (hour,minutes,seconds)
print("time in seconds:")
num=12345
print("converted time in hour ,minutes and seconds is:")
print(convert_time(num))


# In[13]:


#Q2

def avg(list1):
    average=sum(list1)/len(list1)
    return average
list1=[10,20,30,40]
average=avg(list1)
print("average of given number is:",average)
    


# In[20]:


#Q9
string=input("enter the string")
print("original string is",string)
alternative=string[1::2]
print("alternative string is",alternative)


# In[31]:


#Q5

class Maths:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition of two numbers is",self.a+self.b)
    def div(self):
            print("Division of a and b is:",self.a/self.b)
    def sub(self):
        print("substraction of two numbers is",self.a-self.b)
    def Mul(self):
        print("Multiplication of two number is:",self.a*self.b)
obj=Maths(15,3)
obj.add()
obj.div()
obj.sub()
obj.Mul()
    


# In[37]:


#Q7
paise=int(input("enter the paise"))
rupees=paise//100
paise=paise%100
print("Rupees",rupees,"Paise",paise)


# In[50]:


#Q10

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)


# In[41]:


#Q4

arr=["one","two","three"]
def number_to_word(n):
    if (n==0):
        return ""
    else:
        small_ans=arr[n%10]
        ans=number_to_word(int(n/10))+small_ans+" "
        
    return ans
n=int(input())
print("number enter was:",n)
print("converted to word is",end="")
print(number_to_word(n))


# In[49]:


#Q3
k=6
for i in range(1,10,2):
    for j in range(1,i+1):
        if(i==7):
            print(k,end="")
        else:
            print(i,end="")
    print( )


# In[ ]:




