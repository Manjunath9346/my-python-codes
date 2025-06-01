# finding frequency in another method - 1

word = "engineering"
#word = [1,2,3,4,5,6,8,1,2,4,6,8,3,6,2,9,5,4,2]
#word = [5.3, 5.4, 6, 5.4, 5.7, 5.8, 5.5]
res = {}

for ch in word:
    if ch not in res:
        res[ch] = 1
    else:
        res[ch] += 1
#    print(res)
print(res)

sort_res = sorted(res)
sort_res1 = sorted(res.items(), key = lambda tup : tup[0])  # sort based on keys
print(sort_res)
sort_res2 = sorted(res.items(), key = lambda tup: tup[1])  # sort based on values
print(sort_res1)

print(sort_res2)

# find max va;ue in dictionary

max_count = 0
max_char = ''
for key, val in res.items():
    if res[key] > max_count:
        max_count = val
        max_char = key
print(f"The key '{max_char}' has the highest value: '{max_count}'")
