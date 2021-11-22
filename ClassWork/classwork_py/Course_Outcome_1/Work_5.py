#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead

list = []
list = [int(item) for item in input("Enter the list items  ").split()]
print("INPUT IS", list)
x = ["over" if x > 100 else x for x in list]
list = list(x)
print(list)
