class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list[Node]:
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False) -> None:
        new_list = Node(None)
        new_list.next = self.head
        
        curr = self.head
        previous = new_list
        while curr is not None:
            if curr.value != val:
                previous = curr
                curr = curr.next
            else:
                previous.next = curr.next
                if curr == self.tail:
                    self.tail = None if previous.value is None else previous

                curr = previous.next
                if curr is not None:
                    curr.prev = None if previous.value is None else previous
                
                if all == False:
                    break

        self.head = new_list.next

    def clean(self) -> None:
        node = self.head
        while node is not None:
            tmp = node.next
            del node
            node = tmp
            
        self.head = None
        self.tail = None

    def len(self) -> int:
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        
        return length

    def insert(self, afterNode, newNode) -> None:
        if afterNode is None:
            if self.head is None:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            curr = self.head
            while curr is not None:
                if curr == afterNode:
                    tmp = curr.next
                    curr.next = newNode
                    
                    newNode.next = tmp
                    newNode.prev = curr
                    
                    if tmp is not None:
                        tmp.prev = newNode
                        
                    if curr == self.tail:
                        self.tail = newNode

                    break
                else:
                    curr = curr.next

    def add_in_head(self, newNode) -> None:
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode