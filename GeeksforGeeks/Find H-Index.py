class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        m = len(citations)
        h = 0
        for i in range(m):
          if citations[i] >= i+1:
              h = i+1
        return h
