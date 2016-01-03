
class Node(object):
    """docstring for Node"""

    def __init__(self, content, next=None):
        self.content = content
        self.next = next


class Link(object):
    """docstring for Link"""

    def __init__(self, header):
        self.header = header
        self.tail = header

    def insertAtTail(self, node):
        self.tail.next = node
        self.tail = node

if __name__ == '__main__':
    header = Node(10)
    link = Link(header)
    link.insertAtTail(Node(11))
    link.insertAtTail(Node(12))
    tmp = link.header
    while True:
        print tmp.content
        tmp = tmp.next
        if tmp == None:
            break
