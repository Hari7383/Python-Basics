# -*- coding: utf-8 -*-
"""mini calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WsJOtVdSzezAqndmm932FPpSdLCa6JgZ
"""

#make mini calculator
a=int(input()) #get values from user
b=int(input())
o=int(input("add=1/sub=2/div=3/mul=4:")) #o for operations
if(o==1):
  print(a+b)
elif(o==2):
  print(a-b)
elif(o==3):
  print(a/b)
elif(o==4):
  print(a*b)
else:
  print("invalide operator")