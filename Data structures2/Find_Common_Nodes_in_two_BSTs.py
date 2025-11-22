class Solution:
    def findCommon(self, r1, r2):

        s1 = []
        s2 = []
        res = []

        while True:

            # push all left nodes of r1
            while r1:
                s1.append(r1)
                r1 = r1.left

            # push all left nodes of r2
            while r2:
                s2.append(r2)
                r2 = r2.left

            if not s1 or not s2:
                break

            top1 = s1[-1]
            top2 = s2[-1]

            if top1.data == top2.data:
                res.append(top1.data)
                s1.pop()
                s2.pop()
                r1 = top1.right
                r2 = top2.right

            elif top1.data < top2.data:
                s1.pop()
                r1 = top1.right

            else:
                s2.pop()
                r2 = top2.right

        return res
arr1 = [5, 4, None, 3, None, 2, None, 1]
arr2 = [1, None, 2, None, 3, None, 4, None, 5]
# Expected: [1, 2, 3, 4, 5]
