class Solution():
    def __init__(self, n):
        self.n = n
    def solve(self):
        return self.recursion(self.n)
    def recursion(self, n):
        if n <= 2:
            return n
        else:
            return self.recursion(n - 1) + self.recursion(n - 2)
n = int(input())
print(Solution(n).solve()) 

