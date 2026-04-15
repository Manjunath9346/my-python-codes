

'''
s1 = "1101"
s2 = "111"'''
s1 = "01001001"
s2 = "0110101"
write = ""
l = len(s1)-1
k = len(s2)-1
c = 0
while l >= 0 or k >= 0:
    d1 = int(s1[l]) if l >= 0 else 0
    d2 = int(s2[k]) if k >= 0 else 0
    totl = d1 + d2 + c
    if totl == 1:
        write = ('1' + write)
        c = 0
    elif totl == 2:
        write = ('0' + write)
        c = 1
    elif totl == 3:
        write = ('1' + write)
        c = 1
    elif totl == 0:
        write = ('0' + write)
        c = 0
    l -= 1
    k -= 1
if c == 1:
    write = ('1' + write)

write = write.lstrip('0')
if write == "":
    write = 0
print(write)
