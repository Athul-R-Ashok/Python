d={"a":1,"c":5,"b":2,"e":8,"f":4}
print("ASCENDING ORDER : ",sorted(d.items()))
print("DESCENDING ORDER : ", sorted(d.items(),reverse=True))
import operator
dict1=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order:",dict1)
dict1=sorted(d.items(),key=operator.itemgetter(1),reverse=False)
print("Ascending order:",dict1)
