# -*- coding: utf-8 -*-
"""if else.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A-PE7gledZEibwVTsX6-VV9tLHpX9RP8
"""

#if else
if (True): #boolen value True=1
  print("yes")
else:
  print("no")

if (False): #boolen value False=0
  print("yes")
else:
  print("no")

#camparison operator useing if else
a=10
if(a==10):
  print("a is equal to 10")
else:
  print("a is not equal to 10")

#use elif and "and" operator
#student gread system
#35>score poor student
#35<score and 70>score avg student
#35<score and 70<score and score<=100 good student
score=int(input("put your score="))
if(score<=35):
  print("poor student")
elif(score>35 and score<70):
  print("avg student")
elif(score>35 and score>=70 and score<=100):
  print("good student")
else:
  print("invalide score")

#score system
#score>=70 and score<=100 "Get student name,department,and location"
score=int(input("put your score="))
if(score>=70 and score<=100):
  print("you are eligible")
  name=input("Enter your Name:")
  dept=input("Enter your Department:")
  location=input("Enter your Location:")
  print(name,"\n",dept,"\n",location)
else:
  print("you are not eligible")

#loan eligiblity checking using "or" Operator
#salary>20000 or age<=25 "eligible for loan"
a=int(input("Enter your Age:")) #a for Age
s=int(input("Enter your Monthly Salary:")) #s for Salary
if(s>=20000 or a>=25):
  print("you are eligible for loan")
else:
  print("you are not eligible for loan")