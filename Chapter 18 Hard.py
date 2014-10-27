# 18.8
class SuffixTree:
    def __init__(self, string):
        self.root = SuffixTreeNode()
        for i in range(len(string)):
            suffix = string[i:]
            self.root.insert(suffix, i)

    def search(self, target):
        return self.root.search(target)

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

    def insert(self, string, index):
        self.indexes.append(index)
        if string is not None and len(string)!=0:
            value = string[0]
            child = None
            if value in self.children:
                child = self.children[value]
            else:
                child = SuffixTreeNode()
                self.children[value] = child
            remainder = string[1:]
            child.insert(remainder, index)

    def search(self, target):
        if target is None or len(target)==0:
            return self.indexes
        else:
            value = target[0]
            if value in self.children:
                remainder = target[1:]
                return self.children[value].search(remainder)
        return None

class Solution:
    # 18.1
    # 18.2
    # 18.3
    # 18.4
    def count2s(self, num):
        count = 0
        for d in range(len(str(num))):
            count += self.count2sInRangeAtDigit(num, d)
        return count

    def count2sInRangeAtDigit(self, num, d):
        powerOf10 = 10**d
        nextPowerOf10 = powerOf10*10
        right = num%powerOf10
        roundDown = num - num%nextPowerOf10
        roundUp = roundDown + nextPowerOf10
        digit = (num/(10**d))%10
        if digit<2:
            return roundDown/10
        elif digit>2:
            return roundUp/10
        else:
            roundDown/10+right+1

    # 18.5
    # 18.6
    # 18.7
    # 18.8
    def KMP(self, text, pattern):
        # compute longest prefix and suffix array for the pattern
        lps = [0 for i in range(len(pattern))]
        j = 0
        for i in range(1, len(pattern)):
            while j>0 and pattern[i]!=pattern[j]:
                j = lps[j-1]
            if pattern[i]==pattern[j]: j+=1
            lps[i] = j

        # do the search
        t, p = 0, 0 # index for text and pattern
        res = []
        if pattern is None or len(pattern) == 0: return res
        while t<len(text):
            while p>0 and (p == len(pattern) or text[t]!=pattern[p]): 
                if p == len(pattern): res.append(t-p)
                p = lps[p-1]
            if pattern[p]==text[t]: p+=1; t+=1
            if p==0 and pattern[p]!=text[t]: t+=1
        if p == len(pattern): res.append(t-p)
        return res
                
    # 18.9
    # 18.10
    # 18.11
    # 18.12
    # 18.13

if __name__ == "__main__":
    s = Solution()
    # 18.1
    print "# 18.1"
    # 18.2
    print "# 18.2"
    # 18.3
    print "# 18.3"
    # 18.4
    print "# 18.4"
    print s.count2s(99)
    # 18.5
    print "# 18.5"
    # 18.6
    print "# 18.6"
    # 18.7
    print "# 18.7"
    # 18.8
    print "# 18.8"
    t = SuffixTree("banana")
    print t.search("a")
    print s.KMP("banana", "ana")
    print s.KMP("banana", "a")
    print s.KMP("abcdabcd", "cd")
    # 18.9
    print "# 18.9"
    # 18.10
    print "# 18.10"
    # 18.11
    print "# 18.11"
    # 18.12
    print "# 18.12"
    # 18.13
    print "# 18.13"
