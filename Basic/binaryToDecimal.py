a=int(input())
i=0
rem=0
pro=0
sum=0
while a>0:
    rem=int(a%10);
    pro=rem*(2**i)
    i=i+1
    a=int(a/10)
    sum=sum+pro
print(sum)    
