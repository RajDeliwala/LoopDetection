'''
Cracking the coding interview
Chapter 2 - Linked List pg 95
Linked List - Loop detection
----------------------------------------
Question: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop if one exist
Example: A -> B -> C -> D -> E -> C 
input: 
output: Outputs Node C because it is the repeating Node
Constraits or Questions you need to ask:

Solution notes:
Traverse throught the linked list and add data to an hashmap if it doesn't already exist in there. If it exits in the hashmap already return that node
because that is the repeating node

Another solution would be to use 2 pointers, 1 slow 1 fast
if those 2 points ever point at the same node, that means there
is a loop in that linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    #Brute force method to just check if we've already seen this node 
    def loopDetection(self):
        cur = self.head
        lookup = set()
        while cur:
            if cur.data in lookup:
                return print("There is a loop in the linked list and it starts at ", cur.data) 
            lookup.add(cur.data)
            cur = cur.next
        return None
    
    #Using tortoise and hare algo for a O(1) memory solution
    def loopDetectionEfficent(self):
        if not self.head:
            return 
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast.data == slow.data:
                break
        if not fast.next or not fast.next.next:
            return
        slow2 = self.head

        while slow.next:
            if slow.data == slow2.data:
                return print("The cycle exist at data point ", slow.data)      
            slow = slow.next
            slow2 = slow2.next

        return





list1 = LinkedList()

list1.append('A')
list1.append('B')
list1.append('C')
list1.append('D')
list1.append('E')
list1.append('C')

print(list1.loopDetectionEfficent())