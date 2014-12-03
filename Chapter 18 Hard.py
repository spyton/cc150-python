import random;
import heapq;

class Solution:
    # 18.1
    def add(self, a, b):
        if b==0: return a
        sum = a^b
        carry = (a&b)<<1
        return self.add(sum, carry)
    # 18.2
    def shuffleCards(self, cards):
        for i in range(len(cards)):
            j = random.randrange(0, i+1, 1)
            temp = cards[j]
            cards[j] = cards[i]
            cards[i] = temp

    # 18.3
    def randomPick(self, arr, m):
        res = arr[:m]
        for i in range(m, len(arr)):
            j = random.randrange(0, i+1, 1)
            if j<m: res[j] = arr[i]
        return res

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
    def bottomK(self, arr, k):
        temp = [-x for x in arr]
        res = temp[:k]
        heapq.heapify(res)
        for c in temp[k:]:
            if c > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, c)
        return [-x for x in res]

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

if __name__ == "__main__":
    s = Solution()
    # 18.1
    print "# 18.1"
    print s.add(3,4)
    # 18.2
    print "# 18.2"
    a = [1,2,3,4,5]
    print a
    s.shuffleCards(a)
    print a
    # 18.3
    print "# 18.3"
    print s.randomPick([1,2,3,4,5], 3)
    # 18.4
    print "# 18.4"
    print s.count2s(99)
    # 18.5
    print "# 18.5"
    # 18.6
    print "# 18.6"
    print s.bottomK([1,9,2,8,3,4,7,6,5], 3)
    # 18.7
    print "# 18.7"
    # 18.8
    print "# 18.8"
    t = SuffixTree("banana")
    print t.search("a")
    print s.KMP("banana", "ana")
    print s.KMP("banana", "a")
    print s.KMP("abcdabcd", "cd")
    print s.KMP("a", "a")
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
