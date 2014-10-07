class Solution:
    # 1.1
    def uniqueChar(self, str):
        dict = {}
        for c in str:
            if c not in dict:
                dict[c] = True
            else:
                return False
        return True

    # 1.2
    def reverseStr(self, str):
        return str[::-1]

    # 1.3
    def removeDuplicates(self, str):
        if str is None or str == "" or len(str) == 1: return str
        dict = {}
        ss = list(str)
        slow = 0; fast = 0
        while fast != len(ss):
            if ss[fast] not in dict:
                dict[ss[fast]] = True
                ss[slow] = ss[fast]
                fast +=1; slow+=1
            else:
                fast+=1
        return "".join(ss[:slow])

    # 1.4
    def isAnagram(self, str1, str2):
        dict1 = {}; dict2 = {}
        for c in str1:
            dict1[c] = dict1.get(c, 0) + 1
        for c in str2:
            dict2[c] = dict2.get(c, 0) + 1
        if dict1 == dict2: return True
        else: return False
    
    # 1.5
    def replaceChar(self, str):
        ss = list(str)
        for i in range(len(ss)):
            if ss[i] == " ": ss[i] = "%20"
        return "".join(ss)
    
    # 1.6
    def rotateImage(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
 
    # 1.7
    def setZero(self, matrix):
        row = [True for i in range(len(matrix))]
        col = [True for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = False; col[j] = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == False or col[j] == False:
                    matrix[i][j] = 0

    # 1.8
    def isRotation(self, str1, str2):
        if str1 is None and str2 is None: return True
        if len(str1) != len(str2): return False
        str3 = str2 + str2
        return str1 in str3

if __name__ == "__main__":
    s = Solution()
    # print s.uniqueChar("aassbcd")
    # print s.reverseStr("abcd")
    # print s.removeDuplicates(None)
    # print s.removeDuplicates("")
    # print s.removeDuplicates("a")
    # print s.removeDuplicates("aaabbb")
    # print s.removeDuplicates("ababab")
    # print s.removeDuplicates("abcd")
    # print s.isAnagram("shen", "hsne")
    # print s.isAnagram("yes", "nnnsye")
    # print s.replaceChar("nathan shen")
    # a = [[1, 2, 3], [4, 5, 6]]
    # print s.rotateImage(a)
    # a = [[1,1,1], [1,0,1]]
    # s.setZero(a)
    # print a
    print s.isRotation("waterbottle", "erbottlewat")
