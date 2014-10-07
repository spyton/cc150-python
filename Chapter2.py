class Solution:
    # 2.1
    def removeDuplicates(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(-1); dummy.next = head
        current = head.next
        while current is not None:
            check = dummy.next
            prev = dummy
            while check != current:
                if check.val == current.val:
                    prev.next = check.next
                    break
                else:
                    check = check.next
                    prev = prev.next
            current = current.next
        return dummy.next
    
    # 2.2
    def findNthElem(self, head, n):
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        while fast is not None:
            slow = slow.next; fast = fast.next
        return slow.val

    # 2.3
    def deleteNode(self, node):
        if node is None or node.next is None:
            return False
        next = node.next
        node.val = next.val
        node.next = next.next
        return True

    # 2.4
    def addLists(self, list1, list2):
        if list1 is None and list2 is None: return None
        if list1 is None: return list2
        if list2 is None: return list1
        dummy = ListNode(-1); prev = dummy
        carry = 0
        while list1 or list2:
            if list1: carry += list1.val; list1 = list1.next
            if list2: carry += list2.val; list2 = list2.next
            sum = carry%10
            carry = carry/10
            prev.next = ListNode(sum)
            prev = prev.next
        if carry != 0: 
            prev.next = ListNode(carry)
        return dummy.next

    # 2.5
    def findLoop(self, start):
        fast = start
        slow = start
        while True:
            fast = fast.next.next
            slow = slow.next
            if fast is slow: break
        check = start
        while True:
            check = check.next
            slow = slow.next
            if check is slow: break
        return check

if __name__ == "__main__":
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    s = Solution()
    # head = ListNode(1)
    # head.next = ListNode(1)
    # head.next.next = ListNode(1)
    # root = s.removeDuplicates(head)
    # while root is not None:
    #     print root.val,
    #     root = root.next
    # print "\r"
    # ll = [ListNode(x) for x in range(1, 11)]
    # for i in range(9):
    #     ll[i].next = ll[i+1]
    # head = ll[0]
    # print s.findNthElem(head, 2)
    # print s.findNthElem(head, 10)
    # head = ListNode(1)
    # head.next = node = ListNode(2)
    # head.next.next = ListNode(3)
    # s.deleteNode(node)
    # while head is not None:
    #     print head.val,
    #     head = head.next
    # print "\r"
    # a = ListNode(3); a.next = ListNode(1)
    # b = ListNode(9); b.next = ListNode(9); b.next.next = ListNode(9)
    # res = s.addLists(a, b)
    # while res is not None:
    #     print res.val,
    #     res = res.next
    # print "\r"
    ll = [ListNode(x) for x in range(1, 11)]
    for i in range(9):
        ll[i].next = ll[i+1]
    ll[9].next = ll[5]
    head = ll[0]
    node = s.findLoop(head)
    print node.val





















