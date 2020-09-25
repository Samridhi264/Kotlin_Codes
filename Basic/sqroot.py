a=int(input())
#Method 1
# sq=0
# i=1
# while i*i<=a:
#     sq=i
#     i=i+1
# print(sq) 

#Method 2
sq=0
i=1
while i<=int(a/2):
    if int(a/i)==i:
        print(i)
        sq=1
        break
    i=i+1      
if sq==0:
    print("0")
