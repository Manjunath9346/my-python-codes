marks = [23,69,45,67,32,98,65,77,45,35,67]
sum_mar = sum(marks)
l = len(marks)
avg_mar = sum_mar/l

print(f"average marks: {avg_mar:.2f}")

below_marks = 0
above_marks = 0

for i in marks:
    if i < avg_mar:
        print(f"'{i}' is below average marks.")
        below_marks = below_marks + 1
    elif i > avg_mar:
        print(f"'{i}' is above average marks.")
        above_marks = above_marks + 1
    else:
        print(f"'{i}' is average marks.")
print(f"Number of below average marks:'{below_marks}'")
print(f"Number of above average marks:'{above_marks}'")
