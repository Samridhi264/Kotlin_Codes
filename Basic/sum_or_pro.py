num=int(input())
choice=int(input())
if choice==1:
    sum=0
    for i in range(1,num+1,1):
        sum=sum+i
    print(sum)    
elif choice==2:
    pro=1
    for i in range(1,num+1,1):
        pro=pro*i        
    print(pro)    
else:
    print("-1")
