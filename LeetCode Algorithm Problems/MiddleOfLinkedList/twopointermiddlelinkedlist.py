# uses the two pointer slow/fast pattern to find the middle of a linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def main():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(8)
    node5 = Node(13)
    node6 = Node(21)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    # [1] -> [3] -> [5] -> [8] -> [13] -> [21,None]
    
    fast = slow = node1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    print(slow.data)
    return;
  

main()