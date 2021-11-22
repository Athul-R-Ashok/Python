n1,n2,n3=[int(x) for x in input("enter 3 no:s=").split()]
print("Biggest no: =",max(n1,n2,n3))
li=[n1,n2,n3]
li.sort()
print("Biggest no: =",li[-1])