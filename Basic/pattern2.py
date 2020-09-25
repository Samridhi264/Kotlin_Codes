n=int(input())
t=n
g=n
for i in range(1,n+1,1):
    for j in range(t,1,-1):
        print("*",end=" ")
    t=t-1     
    for j in range(1,i+1,1):
        print(j,end=" ")
    for j in range(1,i,1):
        print(j,end=" ")   
    for j in range(g,1,-1):
        print("*",end=" ")
    g=g-1
    print()    
        
