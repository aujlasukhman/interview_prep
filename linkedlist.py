class Node:
    def __init__(self, val, next = None):
            self.val = val
            self.next = next

    def __repr__(self) -> str:
        return str(self.val)

class LinkedList:
    def __init__(self, head = None, ll = None):
        if ll:
            temp = None
            for nodell in ll[::-1]:
                node = Node(nodell)
                node.next = temp
                temp = node

            self.head = node
        else:
            self.head = head

    def __repr__(self):
        node = self.head
        output = []
        while node is not None:
            output.append(str(node.val))
            node = node.next
        output.append('None')
        return ' -> '.join(output)

            

ll = LinkedList(ll = [0,1,2,3,4,5,6,7])
print('linked list is ', ll)
print('linked list head ', ll.head.val)