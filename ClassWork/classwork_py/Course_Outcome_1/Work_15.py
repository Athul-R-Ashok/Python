colorli1=["violet","yellow","blue","white","black"]
colorli2=["violet","black","orange","green","yellow"]
print(colorli1)
print(colorli2)
print("all colors from list1 not contained in list2")
print([x for x in colorli1 if x not in colorli2])
s1=set(colorli1)
s2=set(colorli2)
s3=s1.difference(s2)
print("all colors from list1 not contained list2")
print(list(s3))