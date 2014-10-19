class Solution:
    # 9.1
    def climbStairs(self, n):
        prevprevprev, prevprev, prev = 0, 0, 1
        cur = 0
        for i in range(n):
            cur = prevprevprev + prevprev + prev
            prevprevprev = prevprev
            prevprev = prev
            prev = cur
        return cur

    # 9.2
    def findPath(self, m, n):
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n): dp[0][j] = 1
        for i in range(m): dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    # 9.3
    def findMagic(self, A):
        return self.findMagicRecur(A, 0, len(A))

    def findMagicRecur(self, A, start, end):
        mid = (start+end)/2
        if A[mid] == mid: return mid
        elif A[mid] < mid: return self.findMagicRecur(A, mid+1, end)
        else: return self.findMagicRecur(A, start, mid-1)

    # 9.4
    def subset(self, S):
        current = [[]]
        for s in S:
            next = []
            for c in current:
                next.append(c+[s])
                next.append(c+[])
            current = next
        return current

    # 9.5
    def permutation(self, str):
        if str == "": return [""]
        result = []
        for i in range(len(str)):
            rest = self.permutation(str[:i]+str[i+1:])
            for r in rest:
                result.append(str[i]+r)
        return result

    # 9.6
    def generateParantheses(self, n):
        res = []
        self.generateParenthesesRecur(res, "", n, n)
        return res

    def generateParenthesesRecur(self, res, cur, left, right):
        if left == 0 and right == 0:
            res.append(cur)
        if left > 0:
            self.generateParenthesesRecur(res, cur+"(", left-1, right)
        if left < right:
            self.generateParenthesesRecur(res, cur+")", left, right-1)

    # 9.7
    def paintFill(self, screen, x, y, oldColor, newColor):
        if x <0 or x>len(screen[0])-1: return
        if y<0 or y>len(screen)-1: return
        if screen[x][y] == oldColor:
            screen[x][y] = newColor
            self.paintFill(screen, x-1, y, oldColor, newColor)
            self.paintFill(screen, x+1, y, oldColor, newColor)
            self.paintFill(screen, x, y-1, oldColor, newColor)
            self.paintFill(screen, x, y+1, oldColor, newColor)

    # 9.8
    # 9.9
    # 9.10
    # 9.11


if __name__ == "__main__":
    s = Solution()
    # 9.1
    print "# 9.1"
    print s.climbStairs(3)
    # 9.2
    print "# 9.2"
    print s.findPath(2, 2)
    # 9.3
    print "# 9.3"
    print s.findMagic([-40,-20,-1,1,2,3,5,7,9,12,13])
    # 9.4
    print "# 9.4"
    S = set([1, 2, 3])
    print s.subset(S)
    # 9.5
    print "# 9.5"
    print s.permutation("123")
    # 9.6
    print "# 9.6"
    print s.generateParantheses(3)
    # 9.7
    print "# 9.7"
    screen = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    s.paintFill(screen, 2, 2, 1, 9)
    for s in screen: print s
    # 9.8
    print "# 9.8"
    # 9.9
    print "# 9.9"
    # 9.10
    print "# 9.10"
    # 9.11
    print "# 9.11"
