# # Return bit is 1 or 0
# def getBit(num, i):
#     return num & (1<<i) != 0

# # Set bit to 1 
# def setBit(num, i):
#     return num | (1<<i)

# # Set bit to 0
# def clearBit(num, i):
#     return num & ~(1<<i)

# # Set bits to 0 from most significant bit to i (inclusive)
# def clearBitsMSBtoI(num, i):
#     mask = (1<<i) - 1
#     return num & mask

# # Set bits to 0 from i to lease significant bit (inclusive)
# def clearBitsIto0(num, i):
#     mask = ~((1<<(i+1)-1)
#     return num & mask

# # Set bit to 1 or 0
# def updateBit(num, i, v):
#     mask = ~(1<<i)
#     return (num&mask) | (v<<i)

class Solution:
    # 5.1
    def updateBits(self, n, m, i, j):
        allOnes = ~0
        left = allOnes << (j+1)
        right = (1<<i)-1
        mask = left | right
        n_cleared = n & mask
        m_shifted = m << i
        return n_cleared | m_shifted

    # 5.2
    def printBinary(self, num):
        if num>=1 or num<=0: return "ERROR"
        res = "0."
        while num>0:
            if len(res) > 32: return "ERROR"
            r = num*2
            if r>=1:
                res = res+"1"
                num = r-1
            else:
                res = res+"0"
                num = r
        return res

    # 5.3
    # 5.4
    # 5.5
    # 5.6
    # 5.7
    # 5.8

if __name__ == "__main__":
    s = Solution()
    # 5.1
    print "# 5.1"
    print '{0:b}'.format(s.updateBits(0b10000000000, 0b10011, 2, 6))
    # 5.2
    print "# 5.2"
    print s.printBinary(0.625)
    # 5.3
    # 5.4
    # 5.5
    # 5.6
    # 5.7
    # 5.8


