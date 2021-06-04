# 1. 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        L: List = []
        root = node = ListNode(0)
        while head:
            L.append(head.val)
            head = head.next

        L[left -1: right] = L[right - len(L) - 1: -(len(L) - left + 2):-1]
        
        for i in L:
            node.next = ListNode(i)
            node = node.next
        
        return root.next

# 2. 반복 구조로 노드 뒤집기
def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    # 예외 처리
    if not head or m == n:
        return head
    root = start = ListNode(None)
    root.next = head
    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next