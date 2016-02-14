#for
x=int(input("input an integer:"))
for i in range(1,x+1):
    for j in range(1,x+1):
        print(i,'*',j,'=',i*j)


#while

y=int(input("input an integer:"))

k=1
l=1
while k<=y:
    while l<=y:
        print(k,'*',l,'=',k*l)
        l=l+1
    l=1
    k=k+1
    
