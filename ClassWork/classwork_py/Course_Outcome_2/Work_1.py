n=int(input("enter a no "))
f=1

for x in range(1,n+1):
    f=f*x
print("factorial=",f)

f=1
while n>0:
    f=f*n
    n-=1
print("factorial=",f)