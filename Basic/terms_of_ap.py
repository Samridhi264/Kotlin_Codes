a=int(input())
count=0
num1=1
while count<a:
    num=num1*3+2
    if num%4!=0:
        print(num,end=" ")
        count=count+1    
    num1=num1+1
    
