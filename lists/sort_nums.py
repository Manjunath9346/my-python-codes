
list1 = list(map(int, input("enter a list seperated by space: ").split()))

list2 = []
list3 = []
list4 = []
for i in list1:
    if isinstance(i, int):
        if i != 0:
            list2.append(i)
        elif i == 0:
            list3.append(i)
list4 = list2 + list3
print(list(list4))
