# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:55:09 2023

@author: HP
"""
def my_fanc(lst):
    result = sum((x for x in (y + 1 for y in lst)),10)//3
    return result
numbers= [1, 2, 3, 4, 5]
print(my_fanc(numbers))
#output: 10
s = "awesome"
print(s.replace('e','r', 1))
#output: awrsome
def f1(x):
       x=x+1
       return x
def f2(x):
       x=x+1
       print(x)
r = f1(3)
print(r)
f2(3)

my_set ={1,2,3,4}
my_set.add(5)
print(my_set)
#output: {1,2,3,4,5}

my_tuple =(1, 2, 3, 4)
result = my_tuple +(5,)
print(result)
#output: (1, 2, 3, 4, 5)

def multiply(a, b=2):
    return a* b
result1 = multiply(3)
result2 = multiply(4, 5)
print(result1, result2)
#output:6 20

my_str = ""
not_str = not my_str
my_bool = True or False
print(my_bool == not_str)
#output:True

lst = [1, 2, 3, 4]
another_lst = lst
another_lst[0] = lst.extend({})
print(all(lst) and any(lst))
#output:True

def modify_list(my_list):
    for i in range(len(my_list)):
        my_list[i] += 1
num=[1,2,3]
modify_list(num)
print(num)
#output:[2,3,4]

def change_list(arr):
    arr[-1]='modified'
    return arr
my_l = ['original' ,'values']
print(change_list(my_l))
#output:['original', 'modified']

def multiply(a, b):
    return a * b
res =multiply(3, multiply(2, 4))
print(res)
#output:24

my_set={1, 2, 3}
res=my_set.union({3, 4, 5})
print(res)
#output;{1, 2, 3, 4, 5}















