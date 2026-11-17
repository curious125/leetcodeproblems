class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            sum = n
        else:
            sum = self.fib(n-1) + self.fib(n-2)
        return sum