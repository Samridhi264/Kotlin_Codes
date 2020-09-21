e=int(input())
while e>0:
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
        print(b/c)
    elif a==5:
        b=int(input())
        c=int(input())
        print(b%c)
    elif a==6:
        print("program exist")
    else:
        print("Invalid Operation")
    e=e-1
