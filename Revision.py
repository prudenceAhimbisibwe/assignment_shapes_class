# write a python program that takes a string 
# and returns the reverse of the string.
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
number("my name is prudence and I am 20 years old")
# write a python program that checks
#  if a given string is a pelidrome
def pelidrome_program(z):
     for i in z: 
        y=z[::-1]
        if y==z:
            print("It'a a pelidrome")
        else:
            print("Not a pelidrome")
# pelidrome_program("word")

def word(s):
    y=s[::-1]
    if y==s:
        print("palidrom")
    else:
        print("It's not")
word("mum")




       