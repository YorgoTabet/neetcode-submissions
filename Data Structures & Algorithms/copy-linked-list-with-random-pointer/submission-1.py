"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        initial = head
        count = 0
        copy = []
        node_to_index = {}

        while head:
            # create a copy with no pointer or random
            current = Node(head.val)

            # point the previous node to us, add our node to the array
            if len(copy):
                copy[-1].next = current
            copy.append(current)

            # record with index this node falls on
            node_to_index[head] = count
            count+=1

            # move head
            head = head.next
        # on this pass, check where each node should point and do the connection

        current = initial

        for i in range(len(copy)):
            randomNode = None
            randomIndex = node_to_index.get(current.random, None)

            if(randomIndex is not None and current and current.random):
                randomNode = copy[randomIndex]

            copy[i].random = randomNode

            current = current.next

        return copy[0]
