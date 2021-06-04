# 1. 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        l: List = []
        node = head
        root = new = ListNode(0)
        
        while head:
            l.append(head.val)
            head = head.next
            
        l = l[::2] + l[1::2]
        
        for i in l:
            new.next = ListNode(i)
            new = new.next
            
        return root.next

# 2. 반복 구조로 홀짝 노드 처리
def oddEvenList(self, head: ListNode) -> ListNode:
    # 예외 처리
    if head is NOne:
        return None

    odd = head
    even = head.next
    even_head = head.next


    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀 수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head