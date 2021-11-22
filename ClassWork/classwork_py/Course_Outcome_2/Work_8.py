len=[]
max=[]
for x in range(0,4):
    w=input("enter the word:")
    max.append(len(w))
    len.append(w)
print(len)
print("length of longest word =",max(max))
