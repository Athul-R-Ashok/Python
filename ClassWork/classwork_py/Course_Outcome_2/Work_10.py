n=int(input("Enter a no "))

print("the factors of the number =")
for x in range(1,n+1):
    if n%x==0:
        print(x," ",end="")