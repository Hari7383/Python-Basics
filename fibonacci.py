# -*- coding: utf-8 -*-
"""Fibonacci.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BF1rMhOequS-6kRQf1poo24tFJr4fj9q
"""

n = int(input())
i=2
a = 0
b = 1
if n==1:
  print(a)
if n==2:
  print(a,b)
else:
  print(a,b,end=" ")
  while(i<n):
    print(a+b,end=" ")
    a,b=b,a+b
    i+=1

#alternative easy way
n = int(input())
a = 0
b = 1
c=1
while c<=n:
  print(a+b,end=" ")
  a,b=b,a+b
  c+=1
print(a+b)