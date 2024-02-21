'''
We implement two kinds of Nodes. 
The first one is a node that has only information about the next node.
The second one has information about the next node and the previous node.
'''
class Node:
    _node: any;
    _next_node: any;

    def __init__(self, node: any, next_node: any = None) -> None:
        self._node = node
        self._next_node = next_node

class DoubleNode(Node):
    _previous_node: any;
    _next_node: any;

    def __init__(self, node: any, previous_node: any = None, next_node: any = None) -> None:
        super.__init__(node)
        self._previous_node = previous_node
        self._next_node = next_node
'''
We implement two kinds of Linked List. 
The first one is a linked list that connects has only information about the next node.
The second one has information about the next node and the previous node.
'''
class LinkedList:
    _count: int = 0;
    _header: Node;
    _tail: Node;

    def __init__(self, node: Node = None) -> None:
        self._header = node
        self._tail = node
        if node != None:
            self._count = 1

    def print(self):
        if self._count != 0:
            element: Node = self._header
            while element != self._tail:
                print(f'{element._node} -> ', end='')
                element = element._next_node
            print(f'{element._node}')
        else:
            print('Lista Vazia!!!')

    def add(self, node: Node):
        if self._count == 0:
            self._header = node
            self._tail = node
            self._count = 1
            # print(f'''Header: {self.header.node}
            #           Header_Next: {self.header.next_node}
            #           Tail: {self.tail.node}
            #           Tail_Next: {self.tail.next_node}
            #           Count: {self.count}''')
        else:
            self._tail._next_node = node
            self._tail = node
            self._count += 1
            # print(f'''Header: {self.header.node}
            #           Header_Next: {self.header.next_node}
            #           Tail: {self.tail.node}
            #           Tail_Next: {self.tail.next_node}
            #           Count: {self.count}''')
    def add_at(self, node: Node, position: int):
        if position < 0 or self._count < position:
            print('Posição inválida!')
        else:
            if position == 0:
                node._next_node = self._header
                self._header = node
            elif position == self._count:
                self._tail._next_node = node
                self._tail = node
            else:
                i = 0
                element = self._header
                while i < position - 1:
                    element = element._next_node
                    i += 1
                node._next_node = element._next_node
                element._next_node = node
            self._count += 1


0, 1, 2, 3, 4

if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.add(Node(1))
    ll.print()
    ll.add(Node(2))
    ll.print()
    ll.add(Node(3))
    ll.print()
    ll.add_at(Node(4), -1)
    ll.print()
    ll.add_at(Node(4), 10)
    ll.print()
    ll.add_at(Node(0), 0)
    ll.print()
    ll.add_at(Node(4), 4)
    ll.print()
    ll.add_at(Node(3.5), 4)
    ll.print()
    ll.add_at(Node(1.5), 2)
    ll.print()

                                     

