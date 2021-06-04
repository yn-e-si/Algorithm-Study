# 1. 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = node= ListNode(0)
        L1: str = ''
        L2: str = ''
        while l1:
            L1 += str(l1.val)
            l1 = l1.next
        while l2:
            L2 += str(l2.val)
            l2 = l2.next
        for i in list(map(int,str(int(L1[::-1]) + int(L2[::-1]))))[::-1]:
            node.next = ListNode(i)
            node = node.next
        return root.next

# 2. 자료형 변환 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node

# 3. 전가산기 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

        # 몫(자리올림수) 과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next