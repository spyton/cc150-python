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
    # 17.5
    # 17.6
    # 17.7
    # 17.8
    # 17.9
    # 17.10
    # 17.11
    # 17.12
    # 17.13
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
    # 17.5
    print "# 17.5"
    # 17.6
    print "# 17.6"
    # 17.7
    print "# 17.7"
    # 17.8
    print "# 17.8"
    # 17.9
    print "# 17.9"
    # 17.10
    print "# 17.10"
    # 17.11
    print "# 17.11"
    # 17.12
    print "# 17.12"
    # 17.13
    print "# 17.13"
    # 17.14
    print "# 17.14"
