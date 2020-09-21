i=0
while i<=7: 
    a=int(input())
    if a==1:
        b=int(input())
        c=int(input())
        print(b+c)
    elif a==2:
        b=int(input())
        c=int(input())
        print(b-c)
    elif a==3:
        b=int(input())
        c=int(input())
        print(b*c)
    elif a==4:
        b=int(input())
        c=int(input())
        print(b//c)
    elif a==5:
        b=int(input())
        c=int(input())
        print(b%c)
    elif a==6:
       break
    else:
        print("Invalid Operation")
    i+=1
