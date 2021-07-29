# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:20:51 2021

@author: Admin
"""

#Python program to print positive numbers in a list using for loop:

mylist1 = [10,-20,30,-40,50,-60]
for num in mylist1:
    if num>=0:
        print(num,end=" ")
        
        
        
# Python program to print positive Numbers in a List using while loop:

mylist2 = [23,-4,-14,45,17,-65]
num=0
while(num<len(mylist2)):
    if mylist2[num]>=0:
        print(mylist2[num],end=" ")
    num+=1