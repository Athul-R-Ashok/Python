s=lambda a:a*a
r=lambda l,b:l*b
t=lambda b,h:(b*h)/2

a=int(input("enter side of square"))
l=int(input("enter length of rectangle"))
b=int(input("enter breadth of rectangle"))
b1=int(input("enter breadth of triangle"))
h=int(input("enter height of triangle"))

print("area of square=",s(a))
print("area of square=",r(l,b))
print("area of square=",t(b1,h))