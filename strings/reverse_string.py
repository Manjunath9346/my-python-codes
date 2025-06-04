
# reversing a string without 'reverse()' - function and  '[::-1]'  <-- this method

string = input("enter a string: ")
str_list = list(string)
start, end = 0, len(string)-1

while start < end:
    str_list[start], str_list[end] = str_list[end], str_list[start]
    start = start + 1
    end = end - 1

join = ''.join(str_list)
print(join)
