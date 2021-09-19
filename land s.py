# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 02:00:33 2021

@author: kcs
"""

# List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#types
thislist = ["apple", "banana", "cherry"]
print(type(thislist))

#list constructor
thislist = list(("apple", "banana", "cherry"))#not the double round brackets
print(thislist)

# Access types
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range of indexes
thislist =["apple", "banana", "cherry", "kiwi", "mango ", "melon", "orange"]
print(thislist[2:5])


#strings

print("Hello")
print("Hello")

#assign to a variable
a = "Hello"
print(a)

#multiple strings
a =""" honesty is the best policy"""
print(a)

#arrays
a = "Hello world"
print(a[1])

#looping
for x in "banana":
print(x)

#check string
txt = "Honesty is the best policy"
print(policy in txt)
