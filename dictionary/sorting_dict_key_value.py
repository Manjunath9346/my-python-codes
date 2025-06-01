#Q - sort dictionary in a key wise or value  


my_dict = {'name': 'manju', 'age': 21, 'city': 'paris'}

keys = []
values = []

for k in my_dict.keys():
    keys.append(k)
for v in my_dict.values():
    values.append(v)
sort_keys = sorted(keys)
sort_values = sort_values = sorted([str(v) for v in values])

print(f"sorted keys in my_dict : {sort_keys}")
print(f"sorted values in my_dict : {sort_values}")
