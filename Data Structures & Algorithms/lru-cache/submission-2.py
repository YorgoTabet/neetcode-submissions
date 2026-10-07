class Node:
    def __init__(self, val=None, key=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key


class LRUCache:
    

    def link_to_head(self, current: Node) -> None:
        current.next = self.head.next
        current.prev = self.head
        self.head.next = current
        current.next.prev = current

    def unlink_node(self, current: Node) -> None:
        current.next.prev = current.prev
        current.prev.next = current.next
        current.prev = None
        current.next = None

    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node()
        self.tail = Node()

        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        current = self.map.get(key, None)
    
        if not current:
            return -1

        self.unlink_node(current)
        self.link_to_head(current)

        return current.val

    def put(self, key: int, value: int) -> None:
        current = self.map.get(key, None)
        
        if current:
            self.unlink_node(current)
            self.link_to_head(current)

            current.val = value
        else:
            current = Node(value, key)

            if len(self.map.keys()) == self.capacity:
                to_remove = self.tail.prev

                self.unlink_node(to_remove)

                del self.map[to_remove.key]

            self.link_to_head(current)

            self.map[key] = current
