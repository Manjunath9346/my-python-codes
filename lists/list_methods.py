items = [5, 3, 9, 1, 3]

items.append(10)
items.insert(1, 7)
items.remove(3)  # removes first 3
items.sort()
items.reverse()
count_3 = items.count(3)

print("Final list:", items)
print("Count of 3:", count_3)
