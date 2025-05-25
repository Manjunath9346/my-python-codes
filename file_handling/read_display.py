keyword = "Python"
with open("example.txt", "r") as f:
    for line in f:
        if keyword in line:
            print(line.strip())
