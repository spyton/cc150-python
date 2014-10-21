class Solution:
    # 11.1
    def merge(self, A, B):
        endA = len(A)-1
        endB = len(B)-1
        end = len(A)+len(B)-1
        A.extend([None for i in range(len(B))])
        while endA >= 0 and endB >= 0:
            if A[endA]>B[endB]:
                A[end] = A[endA]
                end-=1; endA-=1
            else:
                A[end] = B[endB]
                end-=1; endB-=1
        if endB >= 0:
            while endB!=0:
                A[end] = B[endB]
                end-=1; endB-=1

    # 11.2
    # 11.3
    def searchRotated(self, A, target):
        start = 0; end = len(A)-1
        while start<=end:
            mid = (start+end)/2
            if A[mid] == target:
                return mid
            if A[mid] < A[start]:
                if target > A[mid] and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid-1
            elif A[mid] > A[start]:
                if target < A[mid] and target >= A[start]:
                    end = mid-1
                else:
                    start = mid+1
            else: # !!!
                start+=1
        return -1

    # 11.4
    # 11.5
    # 11.6
    def searchMatrix(self, matrix, target):
        start = 0
        end = len(matrix)*len(matrix[0])-1
        while start <= end:
            mid = (start+end)/2
            row = mid/len(matrix[0])
            col = mid%len(matrix[0])
            if matrix[row][col] == target:
                return (row, col)
            elif matrix[row][col] > target:
                end = mid-1
            else:
                start = mid+1

    # 11.7
    def longest(self, A):
        B = sorted(A, key=lambda person: person.height)
        dp = [1 for i in range(len(B))]
        for i in range(1, len(B)):
            for j in range(i):
                if B[i].weight > B[j].weight and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
        return max(dp)
            
    # 11.8

if __name__ =="__main__":
    s = Solution()
    # 11.1
    print "# 11.1"
    A = [1,3,5,7,9]
    B = [2,4,6,8,10]
    s.merge(A, B)
    print A
    # 11.2
    print "# 11.2"
    # 11.3
    print "# 11.3"
    print s.searchRotated([1,3,1,1,1], 3)
    # 11.4
    print "# 11.4"
    # 11.5
    print "# 11.5"
    # 11.6
    print "# 11.6"
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print s.searchMatrix(matrix, 7)
    # 11.7
    print "# 11.7"
    class Person:
        def __init__(self, h, w):
            self.height = h
            self.weight = w
    p1 = Person(1,1); p2 = Person(2,3); p3 = Person(3,3); p4 = Person(1,4)
    people = [p1,p2,p3,p4]
    print s.longest(people)     
    # 11.8
    print "# 11.8"