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
    def getNext(self, n):
        c, c0, c1 = n, 0, 0
        while (c!=0) and (c&1==0):
            c0+=1
            c >>= 1
        while c&1==1:
            c1+=1
            c >>=1
        if (c0+c1)==31 or (c0+c1)==0:
            return -1
        p = c0+c1
        n |= (1<<p)
        n &= ~((1<<p)-1)
        n |= (1<<(c1-1))-1
        return n

    def getPrev(self, n):
        c, c0, c1 = n, 0, 0
        while (c&1)==1:
            c1+=1
            c>>=1
        if c == 0: return -1
        while (c&1==0) and c != 0:
            c0+=1
            c>>=1
        p = c0+c1
        n &= ((~0)<<(p+1))
        mask = (1<<(c1+1))-1
        n |= mask<<(c0-1)
        return n

    # 5.4
    # 5.5
    def bitSwapRequired(self, a, b):
        c = a^b
        n = 0
        while (c!=0) and (c&1==1):
            n+=1
            c>>=1
        return n
    # 5.6
    def swapOddEvenBits(self, x):
        return (((x&0xaaaaaaaa)>>1) | ((x&0x55555555) << 1))
    # 5.7
    def findMissing(self, A):
        return self.findMissingRecur(A)

    def findMissingRecur(self, A):
        if sum(A) == 0: return 0
        zeros, ones = [], []
        for a in A:
            if (a&1)==1:
                a>>=1
                ones.append(a)
            else:
                a>>=1
                zeros.append(a)
        if len(zeros) <= len(ones):
            # LSB of x is 0
            v = self.findMissingRecur(zeros)
            return (v<<1)|0
        else:
            # LSB of x is 1
            v = self.findMissingRecur(ones)
            return (v<<1)|1
    # 5.8
    def drawLine(self, screen, width, x1, x2, y):
        start_offset = x1%8
        first_full_byte = x1/8
        if start_offset != 0: first_full_byte+=1
        end_offset = x2%8
        last_full_byte = x2/8
        if end_offset != 7: last_full_byte-=1
        # set full bytes
        for i in range(first_full_byte, last_full_byte+1):
            screen[(width/8)*y + i] = 0xff
        # create masks for start and end of line
        start_mask = 0xff >> start_offset
        end_mask = (0xff >> (end_offset+1))^0xff
        print "{:08b}".format(start_mask)
        print "{:08b}".format(end_mask)
        print end_offset
        # set start and end of line
        if (x1/8) == (x2/8):
            mask = start_mask & end_mask
            screen[(width/8)*y+(x1/8)] |= mask
        else:
            if start_offset != 0 :
                screen[(width/8)*y+first_full_byte-1] |= start_mask
            if end_offset != 7:
                screen[(width/8)*y+last_full_byte+1] |= end_mask

if __name__ == "__main__":
    s = Solution()
    # 5.1
    print "# 5.1"
    print '{0:b}'.format(s.updateBits(0b10000000000, 0b10011, 2, 6))
    # 5.2
    print "# 5.2"
    print s.printBinary(0.625)
    # 5.3
    print "# 5.3"
    n = 0b11011001111100
    print '{0:b}'.format(n)
    print '{0:b}'.format(s.getNext(n))
    n = 0b10011110000011
    print '{0:b}'.format(n)
    print '{0:b}'.format(s.getPrev(n))
    # 5.4
    # 5.5
    print "# 5.5"
    a = 0b1100
    b = 0b0011
    print '{0:b}'.format(a), '{0:b}'.format(b)
    print s.bitSwapRequired(a, b)
    # 5.6
    print "# 5.6"
    a = 0b10101010
    print "{0:b}".format(a)
    print "{0:b}".format(s.swapOddEvenBits(a))
    # 5.7
    print "# 5.7"
    print s.findMissing([0,1,2,3,4,5,7,8,9,10])
    # 5.8
    print "# 5.8"
    screen = [0b00000000, 0b00000000, 0b00000000, 0b00000000]
    s.drawLine(screen, 16, 3, 13, 0)
    cur = 0
    while cur < len(screen):
        print "{:08b}".format(screen[cur]),
        cur+=1
        print "{:08b}".format(screen[cur])
        cur+=1
