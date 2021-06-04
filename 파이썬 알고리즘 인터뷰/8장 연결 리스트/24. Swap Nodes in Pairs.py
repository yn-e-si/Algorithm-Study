# 1. 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = head
        while head and head.next:
            
            head.val, head.next.val = head.next.val, head.val
            
            head = head.next.next
        return start

# 2. 반복 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b 가 a (head) 를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev 가 b 를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next

# 3. 재귀 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head