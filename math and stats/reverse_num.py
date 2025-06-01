# reversing a number using modular arithmatic

num = int(input("enter a number: "))

rev_num = ''
res = 0
rem = 0
while num != 0:
    rem = num % 10
    rev_num = rev_num + str(rem)
    num= num // 10
print(rev_num)
