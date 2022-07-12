# 1. Write a Python program to calculate the length of a string.
def calculate_length():
    x="Akirachix"
    z=len(x)
    print (z)
calculate_length()

# 2. Write a Python program to count the number of characters 
# (character frequency) in a string
def count_number(str):
    dict={}
    for x in str:
        keys=dict.keys()
        if x in keys:
            dict[x]+=1
        else:
            dict[x]=1
        return dict
print(count_number("lovelace"))

# 3. Write a Python program to get a string made 
# of the first 2 and the last 2 chars from a given a string. If the string 
# length is less than 2, return instead of the empty string.
# from turtle import right


def concatinate(z):
    if len(z)<2:
        return ""
    else:
        print(z[0:2]+z[-2:])
concatinate("akirachix")


# 5. Write a Python program to get a single string 
# from two given strings, separated by a space and
#  swap the first two characters of each string
def program():
    x="Akira"
    y="Chix"
    print (x+""+y)
program()
# 6. Write a Python program to add 'ing' at the end
#  of a given string (length should be at least 3) 
# If the given string already ends with 'ing'
#  then add 'ly' instead. If the string length of the given 
# string is less than 3, leave it unchanged.

def program():
    a=str(input("Enter the word"))
    x=len(a)
    if x>=3:
        if a[-3:]=="ing":
            a+="ly"
        else:
            a+="ing"
    print(a)
program()

# A pyhton program to swap the first and the last number of a list
# from tabnanny import check.

def swap_list():
    x=[2,7,9,10]
    x[0],x[-1]=x[-1],x[0]
    print (x)
swap_list()
# A python program that prints the multiplication table  between 1 to 10
def multiplication_table():
    number=int(input("Enter your number:"))
    x=range(1,11)
    for i in x:
         print(str(number) + " X " + str(i) + " = " + str(i*number))
multiplication_table()

# multiplicatin table:
def multiplication():
    number=11
    for i in range(number):
        print()
        for j in range(number):
            print(i*j,end="\t")
multiplication()

def arrange():
    detail={"prude":34,"Jane":40,"Anena":20}
    print(sorted(detail.items()))
arrange()

def word(s):
    y=s[::-1]
    if y==s:
        print("palidrom")
    else:
        print("It's not")
word("mum")

def names(s):
    x= s.pop()
    print(x)
names(["Jane","prude","Joy","Anena","Judy"])

# Assessment revision

# write a python function that takes in argument as
#  alist a=[2,4,6,8]and remove the second last item
#  from that listand returns the whole list without the removed item
def remove_program(a):
    a.pop(-2)
    print(a)
remove_program([2,3,4,5,6,7])

# write a python program that 
# have a list of days =["monday","Tuesday","Thursday","monday"]

def count_occurance_program():
    days=["monday","Tuesday","Thursday","monday"]
    x=days.count("monday")
    print(x)
count_occurance_program()

# write  python function named smallest that accepts
#  a list of unsorted integers and returns the smallest number in the list

def smallest():
    a=[3,5,6,2,8,4,9,7,1]
    y=sorted(a)
    small=y[0]
    print(small) 
smallest()

# write a function named divisible_by_seven that ;
# using the range function and a loop returns a list
# containing all the numbers btn 100 and 200 that are divisible by 7

def divisible_program():
    for i in range(100,200):
        if i%7==0:
          print(i)
divisible_program()
# write a python program that takes in two
# inputs(as integers )from a user and adds 
# the two numbers,checks if the sum is 
# greater than 10,less than 10 or equal
#  to 10 and prints a statement after each check 

def check_program():
    a=int(input("Enter number1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ))
    b=int(input("Enter number2"))
    add=a+b
    if add>10:
      print("greater than 10")
    elif add<10:
      print("less than 10")
    else:
        add==10
        print("equal to 10")
check_program()

def number():
    x="They are students at Akirachix"
    y=len(x)//2
    z=x[0:y].upper()
    w=x[y: ]
    p=z+w
    print(p)
number()

# write a python function that takes one argument 
# which is a list ,a=[1,2,3,4,5]and returns
#  true if 4 is present in the list and false
#  if 4 is not present in the list.

def check_out(a):
      if 4 in a:
            print(True)
      else:
            print(False)
check_out([1,2,3,4,5])

# White a fuction that takes in an argument
#  which is a list fruits=["apple","grapes","pineaple"]
#  and removes the last fruit from the list then returns the list 
# without the removed fruit.

def fruit_remove(fruits):
    fruits.pop()
    print(fruits)
fruit_remove(["apple","grapes","pineaple"])

# write a python program that takes in a list of cars ,
# cars=["ford","BMW","volve",] and returns a sorted list.

def arrange_program(cars):
   cars.sort()
   print(cars)
arrange_program(["ford","bMW","volve"]) 

def number():
    x=[1,1,2,3,5,13,21,24]
    for i in x:
       if i <5:
        print(i,end="")
number()

def long ( ):
    y=["prudence","gfs","sfhsaf","sfads"]
    d=0
    for i in y:
      d+=1
    print(d) 
long() 

def program():
   y=[1,2,3,4,5,6,7]
   y[0],y[1],y[2],y[3],y[4],y[5],y[6]=y[6],y[5],y[4],y[3],y[2],y[1],y[0]
   print(y)


def number():
  x=[1,2,3,4,1,2,3,5,6,7]
  y=[]
  for i in x:
     if i not in y:
      y.append(i)
      x=y    
  print(x) 
number()

def number(a):
  y=[]
  for i in a:
    if i not in y:
      y.append(i)
      a=y
  print(a)
number([1,2,3,4,1,2,3,5,6,7,8,9])

def word():
  x="prudence"
  y=""
  for i in x :
    if i not in y:
      y=y+i
  print(y)
word()

def character():
  word="they are students at akirachix"
  z=word.swapcase()
  print(z)
character()

def number(y):
     x = y.split()
     start=0
     end=len(x)-1
     while start<end:
        x[start],x[end]=x[end],x[start]
        start+=1
        end-=1
        str=" "
     print(str.join(x))
number("my name is prudence")


def program(list1):
    x=list1.split()
    list2 =[]
    while x != []:
       poppedItem = x.pop()
       list2.append(poppedItem)    
    print(" ".join(list2))
# program("my name is prudence and I am a student at Akirachix")

def program(x):
    y=x.split()
    z=[]
    while y!=[]:
        w=y.pop()
        z.append(w)
    print(" ".join(z))
# program("Linda is the lead of Akirachix")

def pelidrome(x):
  left=0
  right=len(x)-1
  while left<right:
    if left!=0:
      print("Not a pelidrome")
    else:
      print("It's a pelidrome")
      left+=1
      right-=1
pelidrome("mum")

# Write a function that takes in an array of integers and returns the product of
# all the elements
# (3pts)

def mult(x):
    result=1
    for i in x:
        result =(i*result)
        print(result)
mult([2,3,4,5,6,7,8])    



        






          