def count_number():
    number=65789
    count=0
    while number!=0:
        number //=10
        count+=1
count_number()