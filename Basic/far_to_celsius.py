start=int(input())
end=int(input())
step=int(input())
while start<=end:
    cel=int((start-32)*5/9)
    print(start,cel)
    start=start+step
    
