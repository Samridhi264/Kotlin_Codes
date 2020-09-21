num=int(input())
rev=0
num1=num
while num>0:
    rem=int(num%10)
    num=int(num/10)
    rev=10*rev+rem
# print(rev)
if num1==rev:
    print("true")
else:
    print("false")
          
