class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    

def printNode(node):
    curt_node = node
    while curt_node is not None:
        print(curt_node.val, end=' ')
        curt_node = curt_node.next
    
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        
        
    def addAtHead(self, val):
        node = ListNode(val)  # 넘어온 val 값으로 새로운 노드를 만들어준다.
        node.next = self.head # 새로 넘어온 노드 next에 헤드가 가리키고있던곳을 넣어준다.
        self.head = node # 이 헤드는 새롭게 만들어진 노드를 가르킨다.
        
    def addBack(self,val):
        node = ListNode(val) # 새로운 노드를 만들어주고
        curt_node = self.head # 현재노드를 head로 부터 시작하게한다.
        while curt_node.next: # curt 노드가 next val값을 가지고있을때까지 계속되고
            curt_node = curt_node.next # 노드의 위치를 끝으로 옮겨줌
        curt_node.next = node #next는 새로만들어진 노드를 가르키면됨
            
        
        

slist = SLinkedList()
slist.addAtHead(1) # 1
slist.addAtHead(2) # 2 1
slist.addAtHead(3) # 3 2 1
slist.addBack(4) # 3 2 1 4
printNode(slist.head)


        