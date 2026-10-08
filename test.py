from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = []
        pre = 0
        for c in s:
            nc = ord(c)-ord('a')
            diff.append(nc - pre)
            pre = nc
        diff.append(0)
        for st, end, direct in shifts:
            d = 1 if direct else -1
            diff[st] += d
            diff[end+1] -= d
        ans = []
        sm = 0
        for x in diff:
            c = chr((x+sm+26)%26 + ord('a'))
            ans.append(c)
            sm += x
        ans.pop()
        return ''.join(ans)

if __name__ == '__main__':
    sol = Solution()
    print(sol.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))