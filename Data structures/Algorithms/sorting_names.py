# sorting a list of names without using 'sorted()' function. using - selection sort

names = ['manju', 'pavan', 'aruna', 'sai', 'nitheesh', 'prashu']
n = len(names)

for i in range(0, n, 1):
    for j in range(i+1, n, 1):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]
print(f"sorted names: {names}")
