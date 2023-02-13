# 싱글링크드리스트 구현 -> 더블링크드리스트구현하면
# 더블링크드리스트가 이해가될것이야!

# 싱글링크드리스트에는 val값과 next노드값이 필요하다.

class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        
head_node = ListNode(1)  # headnode = val = 1 , next = x
head_node.next = ListNode(2) # headnode의 next가 두번째 노드를 가르킴
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)


# 1. iterater
def printNodes(node):   #:ListNode 주석 생략
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val , end = ' ')
        crnt_node =crnt_node.next
        

# 2. recursive
def printNodeRecur(node):
    print(node.val, end=' ')
    if node.next is not None:
        printNodeRecur(node.next)
        
        
printNodeRecur(head_node)
    

