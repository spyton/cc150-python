class Solution:
    # 4.1
    def isBalanced(self, root):
        return self.isBalancedRecur(root)[0]

    def isBalancedRecur(self, root):
        if root is None: return (True, 0)
        left = self.isBalancedRecur(root.left)
        right = self.isBalancedRecur(root.right)
        if left[0] == False or right[0] == False or abs(left[1]-right[1])>1:
            return (False, max(left[1], right[1])+1)
        else:
            return (True, max(left[1], right[1])+1)

    # 4.2
    # pass
    # 4.3
    def createBST(self, array):
        return self.createBSTRecur(array)

    def createBSTRecur(self, array):
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return TreeNode(array[0])
        else:
            mid = len(array)/2
            root = TreeNode(array[mid])
            root.left = self.createBSTRecur(array[:mid])
            root.right = self.createBSTRecur(array[mid+1:])
            return root

    # 4.4
    def connect(self, root):
        current = [root]
        while len(current) != 0:
            next = []
            while len(current) != 0:
                node = current.pop(0)
                if len(current) != 0:
                    node.next = current[0]
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            current = next
    # 4.5
    def isBST(self, root):
        return self.isBSTRecur(root, -9223372036854775808, 9223372036854775807)

    def isBSTRecur(self, root, min, max):
        if root is None: return True
        if root.left is None and root.right is None:
            return root.val > min and root.val < max
        if root.left is None:
            return self.isBSTRecur(root.right, root.val, max) and root.val > min
        if root.right is None:
            return self.isBSTRecur(root.left, min, root.val) and root.val < max
        return self.isBSTRecur(root.left, min, root.val) and self.isBSTRecur(root.right, root.val, max)

    # 4.6
    def findNext(self, root):
        if root.right is not None:
            next = root.right
            while next.left is not None:
                next = next.left
            return next
        else:
            current = root
            next = root.parent
            while next is not None:
                if next.left == current:
                    break
                else:
                    next = next.parent
                    current = current.parent
            return next
    # 4.7
    def findLCA(self, root, p, q):
        if root is None: return None
        if root == p or root == q: return root
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        if left and right: return root
        elif left: return left
        else: return right

    # 4.8
    def isSubtree(self, T1, T2):
        if T2 is None: return True
        if T1 is None: return False
        if T1.val == T2.val:
            if self.matchTree(T1, T2): return True
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def matchTree(self, T1, T2):
        if T1 is None and T2 is None: return True
        if T1 is None or T2 is None: return False
        if T1.val != T2.val:
            return False
        else:
            return self.matchTree(T1.left, T2.left) and self.matchTree(T1.right, T2.right)

    # 4.9
    def findPath(self, root, target):
        res = []
        self.findPathRecur(res, [], root, target)
        return res

    def findPathRecur(self, res, cur, root, target):
        if root is None: return
        if root.val == target:
            res.append(cur+[root.val])
        self.findPathRecur(res, [], root.left, target)
        self.findPathRecur(res, [], root.right, target)
        self.findPathRecur(res, cur+[root.val], root.left, target-root.val)
        self.findPathRecur(res, cur+[root.val], root.right, target-root.val)

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    class TreeLinkNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.next = None
    class TreeParentNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.parent = None
    s = Solution()
    # 4.1
    print "# 4.1"
    root = TreeNode(0)
    print s.isBalanced(root)
    root.left = TreeNode(1)
    print s.isBalanced(root)
    root.right = TreeNode(2)
    print s.isBalanced(root)
    root.right.right = TreeNode(3)
    print s.isBalanced(root)
    root.right.right.left = TreeNode(4)
    print s.isBalanced(root)
    # 4.2
    # 4.3
    print "# 4.3"
    root = s.createBST([1,2,3])
    print root.left.val, root.val, root.right.val
    root = s.createBST([1,2,3,4])
    print root.left.left.val, root.left.val, root.val, root.right.val
    # 4.4
    print "# 4.4"
    root = TreeLinkNode(1); root.left = TreeLinkNode(2); root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4); root.right.right = TreeLinkNode(7)
    s.connect(root)
    print root.left.left.next.val
    # 4.5
    print "# 4.5"
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print s.isBST(root)
    root.right.left = TreeNode(1.5)
    print s.isBST(root)
    # 4.6
    print "# 4.6"
    root = TreeParentNode(1); root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.parent = root; root.right.parent = root
    print s.findNext(root).val, s.findNext(root.left).val
    root.left.right = TreeNode(4); root.left.right.parent = root.left
    print s.findNext(root.left.right).val
    # 4.7
    print "# 4.7"
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    p = root.left.left = TreeNode(4); q = root.left.right = TreeNode(5)
    print s.findLCA(root, p, q).val
    # 4.8
    print "# 4.8"
    T1 = TreeNode(1)
    T1.left = TreeNode(2); T1.right = TreeNode(3)
    T1.left.left = TreeNode(4); T1.left.right = TreeNode(5)
    T2 = TreeNode(2)
    T2.left = TreeNode(4); T2.right = TreeNode(5)
    print s.isSubtree(T1, T2)
    # 4.9
    print "# 4.9"
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(0)
    print s.findPath(root, 2)