z=int(input("Enter the upper limit="))
r=int(input("Enter the lower limit="))
li=[]
li1=[]

for x in range(r, z + 1):
    if x % 2 == 0:
        li.append(x)

for y in li:
    for z in range(1,y):
          if (z*z) ==y:
             li1.append(y)
print(li1)

