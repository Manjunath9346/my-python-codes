class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * self.size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x

    def push2(self, x):
        if self.top1 + 1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x

    def pop1(self):
        if self.top1 >= 0:
            val = self.arr[self.top1]
            self.top1 -= 1
            return val
        return -1

    def pop2(self):
        if self.top2 < self.size:
            val = self.arr[self.top2]
            self.top2 += 1
            return val
        return -1
# Test Case 1
ts = TwoStacks(10)
ts.push1(2)
ts.push1(3)
ts.push2(4)
print(ts.pop1())  # Output: 3
print(ts.pop2())  # Output: 4
print(ts.pop2())  # Output: -1

# Test Case 2
ts = TwoStacks(10)
ts.push1(1)
ts.push2(2)
print(ts.pop1())  # Output: 1
ts.push1(3)
print(ts.pop1())  # Output: 3
print(ts.pop1())  # Output: -1

# Test Case 3
ts = TwoStacks(10)
ts.push1(2)
ts.push1(3)
ts.push1(4)
print(ts.pop2())  # Output: -1
print(ts.pop2())  # Output: -1
print(ts.pop2())  # Output: -1
