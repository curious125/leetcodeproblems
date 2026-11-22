class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        l = [a,b,c]
        l.sort()
        if l[2] > (l[1] + l[0]):
            l[2] = l[1] + l[0]
        return max(l[0],l[1],l[2]) - min(l[0],l[1],l[2])   