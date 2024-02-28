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
'''
class LinkedList:
    _count: int = 0;
    _header: Node;
    _tail: Node;

    '''
    Creates a LinkedList containing the Node node and defining its header and tail as this node 
    '''
    def __init__(self, node: Node = None) -> None:
        self._header = node
        self._tail = node
        if node != None:
            self._count = 1

    '''
    Prints all elements of the LinkedList with format a -> b -> c -> ... -> z
    '''
    def print_list(self):
        if self._count != 0:
            element: Node = self._header
            while element != self._tail:
                print(f'{element._node} -> ', end='')
                element = element._next_node
            print(f'{element._node}')
        else:
            print('Lista Vazia!!!')

    def traverse_list(self, final_position: int):
        i = 0
        element = self._header
        while i < final_position:
            element = element._next_node
            i += 1
        return element
    '''
    Given an element ref_node in the LinkedList, adds a new element right after it.
    '''
    def _add_node_after(self, new_node: Node, ref_node: Node):
        new_node._next_node = ref_node._next_node
        ref_node._next_node = new_node

    '''
    This is the function that adds an element to the LinkedList. 
    It can receive a parameter position to determine the position to which the new element should be inserted.
    if no value is passed on position, it adds the new element in the last position.
    '''
    def add_node(self, new_node: Node, position: int = -1):
        if self._count == 0:
            self._header = new_node
            self._tail = new_node
        elif position == 0:
            new_node._next_node = self._header
            self._header = new_node
        elif position == self._count or position == -1:
            self._tail._next_node = new_node
            self._tail = new_node
        else:
            element = self.traverse_list(position-1)
            self._add_node_after(new_node=new_node, ref_node=element)
        self._count += 1

    '''
    Function to add new node in a defined position
    '''
    def add_node_at(self, node: Node, position: int):
        if position < 0 or self._count < position:
            print('Posição inválida!')
        else:
            self.add_node(node, position)

    def print_node(self, position: int, node: Node, message: str):
        if position < 0 or self._count <= position:
            print('Posição inválida!')
        else:
            print(message.format(position=position, node=node._node))

    def get_node_at(self, position: int):
        message = "O node na posição {position} é o {node}."
        if position < 0 or self._count <= position:
            print('Posição inválida!')
        else:
            element = self.traverse_list(position)
            self.print_node(position, element, message)
                

    def set_node_at(self, node: Node, position: int):
        if position < 0 or self._count <= position:
            print('Posição inválida!')
        else:
            element = self.traverse_list(position)
            element._node = node._node

    def remove_node(self, node: Node):
        message = "Node {node} removido da posição {position}."
        position = 0
        last_node = Node(None)
        present_node = self._header
        while present_node != None:
            if present_node._node == node._node:
                if present_node == self._header:
                    self._header = self._header._next_node
                    self.print_node(position, node, message)
                else:
                    last_node._next_node = present_node._next_node
                    self.print_node(position, node, message)
                return 0
            else:
                last_node = present_node
                present_node = present_node._next_node
                position += 1
        print(f'O node {node._node} não foi localizado na lista.')
        return -1



if __name__ == '__main__':
    ll = LinkedList()
    ll.print_list()
    ll.add_node(Node(1))
    ll.print_list()
    ll.add_node(Node(2))
    ll.print_list()
    ll.add_node(Node(3))
    ll.print_list()
    ll.add_node_at(Node(0), -1)
    ll.print_list()
    ll.add_node_at(Node(0), 10)
    ll.print_list()
    ll.add_node_at(Node(0), 0)
    ll.print_list()
    ll.add_node_at(Node(4), 4)
    ll.print_list()
    ll.add_node_at(Node(3.5), 4)
    ll.print_list()
    ll.add_node_at(Node(1.5), 2)
    ll.print_list()
    ll.get_node_at(-1)
    ll.get_node_at(0)
    ll.get_node_at(2)
    ll.get_node_at(6)
    ll.get_node_at(7)
    ll.print_list()
    ll.set_node_at(Node(5), -1)
    ll.print_list()
    ll.set_node_at(Node(5), 0)
    ll.print_list()
    ll.set_node_at(Node(6), 2)
    ll.print_list()
    ll.set_node_at(Node(6), 7)
    ll.print_list()
    ll.add_node(Node(2))
    ll.print_list()
    ll.remove_node(Node(-1))
    ll.print_list()
    ll.remove_node(Node(5))
    ll.print_list()
    ll.remove_node(Node(2))
    ll.print_list()
                                     

