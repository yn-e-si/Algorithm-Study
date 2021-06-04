# 1. Deque 사용
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False

        l = collections.deque()

        node = head

        while node is not None:
            l.append(node.val)
            node = node.next
            
        for _ in range(len(l)//2):
            left = l.popleft()
            right = l.pop()
            if left != right:
                return False
        else:
            return True


# 2. List 사용
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l: List = []
        if not head:
            return True
            
        node = head
        while node is not None:
            l.append(node.val)
            node = node.next
            
        while len(l) >1:
            if l.pop(0) != l.pop():
                return False

        return True

# 3. 파이써닉 방식
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        node = head

        while node is not None:
            l.append(node.val)
            node = node.next   
               
        return l == l[::-1]

# 4. 러너를 이용한 방식
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
       rev = None
       slow = fast = head

       # 런너를 이용해 역순 연결 리스트 구성
       while fast and fast.next:
           fast = fast.next.next
           rev, rev.next, slow = slow, rev, slow.next
        # 주어진 연결 리스트가 홀 수일 경우 중간의 값을 피하기 위한 코드
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev