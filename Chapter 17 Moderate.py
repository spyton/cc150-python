class Solution:
    # 17.1
    def swap(self, a, b):
        print a, b
        a = a^b
        b = a^b
        a = a^b
        print a, b

    # 17.2
    # 17.3
    def countZeros(self, num):
        count = 0
        if num<0: return -1
        i = 5
        while num/i>0:
            count += num/i
            i *= 5
        return count

    # 17.4
    def flip(self, b):
        return 1^b

    def sign(self, a):
        return self.flip((a>>31)&1)

    def getMax(self, a, b):
        c = a - b
        sign_a = self.sign(a)
        sign_b = self.sign(b)
        sign_c = self.sign(c)
        use_sign_a = sign_a^sign_b
        use_sign_c = self.flip(use_sign_a)
        k = use_sign_a*sign_a+use_sign_c*sign_c
        q = self.flip(k)
        return a*k+b*q

    # 17.5
    # 17.6
    def findLeftEnd(self, arr):
        for i in range(1, len(arr)):
            if arr[i]<arr[i-1]: return i-1
        return len(arr)-1

    def findRightStart(self, arr):
        for i in reversed(range(1, len(arr))):
            if arr[i-1]>arr[i]: return i
        return 0

    def shinkLeftEnd(self, arr, left_end, v_min):
        for i in range(left_end+1):
            if arr[i] > v_min: return i-1
        return left_end

    def shinkRightStart(self, arr, right_start, v_max):
        for i in reversed(range(right_start, len(arr))):
            if arr[i]<v_max: return i+1
        return right_start

    def findUnsorted(self, arr):
        left_end = self.findLeftEnd(arr)
        right_start = self.findRightStart(arr)
        v_min = arr[left_end+1]; v_max = arr[right_start-1]
        for i in range(left_end+1, right_start):
            if arr[i]<v_min: v_min = arr[i]
            if arr[i]>v_max: v_max = arr[i]
        left_end = self.shinkLeftEnd(arr, left_end, v_min)
        right_start = self.shinkRightStart(arr, right_start, v_max)
        return (left_end+1, right_start-1)
    
    # 17.7
    # 17.8
    def findLargestSum(self, arr):
        max_sum = -9223372036854775808
        sum_so_far = 0
        for d in arr:
            if sum_so_far < 0 : sum_so_far = 0
            sum_so_far += d
            max_sum = max(max_sum, sum_so_far)
        return max_sum

    # 17.9
    # 17.10
    # 17.11
    # 17.12
    def twoSum(self, arr, target):
        hash = {}
        for i in range(len(arr)):
            comp = target - arr[i]
            if comp in hash: return (hash[comp], i+1)
            else: hash[arr[i]] = i+1
        return (-1, -1)
    # 17.13
    def convert(self, root):
        if root is None: return None
        return self.convertRecur(root)[0]

    def convertRecur(self, root):
        start = root
        if root.node1:
            left = self.convertRecur(root.node1)
            left[1].node2 = root; root.node1 = left[1]
            start = left[0]
        end = root
        if root.node2:
            right = self.convertRecur(root.node2)
            right[0].node1 = root; root.node2 = right[0]
            end = right[1]
        return (start, end)
    # 17.14

if __name__ == "__main__":
    s = Solution()
    # 17.1
    print "# 17.1"
    s.swap(1, 10)
    # 17.2
    print "# 17.2"
    print s.countZeros(19)
    # 17.3
    print "# 17.3"
    # 17.4
    print "# 17.4"
    print s.getMax(10, -6)
    print s.getMax(10, 6)
    print s.getMax(-6, -10)
    # 17.5
    print "# 17.5"
    # 17.6
    print "# 17.6"
    print s.findUnsorted([1,2,3,4,7,5])
    # 17.7
    print "# 17.7"
    # 17.8
    print "# 17.8"
    print s.findLargestSum([-2,1,-3,4,-1,2,1,-5,4])
    # 17.9
    print "# 17.9"
    # 17.10
    print "# 17.10"
    # 17.11
    print "# 17.11"
    # 17.12
    print "# 17.12"
    print s.twoSum([1,3,2,4], 6)
    # 17.13
    print "# 17.13"
    class BiNode:
        def __init__(self, v):
            self.val = v
            self.node1 = None
            self.node2 = None
    root = BiNode(4)
    root.node1 = BiNode(2); root.node1.node1=BiNode(1); root.node1.node2 = BiNode(3)
    root.node2 = BiNode(5); root.node2.node2 = BiNode(6)
    head = s.convert(root)
    current = head
    while current is not None:
        print current.val,
        current = current.node2
    print "\n"
    # 17.14
    print "# 17.14"
