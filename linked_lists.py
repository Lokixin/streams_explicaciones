

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class EmptyLinkedListException(Exception):
    pass


class NodeNotFoundException(Exception):
    pass


class LinkedList:
    def __init__(self, nodes: list = None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first_node(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def add_last_node(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node is not None:
            if last_node.next is None:
                last_node.next = node
                break
            last_node = last_node.next

    def insert_after_node(self, target_node_value, new_node_value) -> None:
        if self.head is None:
            raise EmptyLinkedListException("The linked list is empty")
        for target_node in self:
            if not target_node.data == target_node_value:
                continue
            new_node = Node(data=new_node_value)
            new_node.next = target_node.next
            target_node.next = new_node
            return
        raise NodeNotFoundException(f"Node with value {target_node_value} does not exist")

    def insert_before_node(self, target_node_value, new_node_value) -> None:
        if self.head is None:
            raise EmptyLinkedListException("The Linked list is empty")
        if self.head.data == target_node_value:
            self.add_first_node(Node(data=new_node_value))
            return
        for target_node in self:
            if not target_node.next:
                raise NodeNotFoundException(f"Node with value {target_node_value} does not exist")
            if not target_node.next.data == target_node_value:
                continue
            new_node = Node(data=new_node_value)
            new_node.next = target_node.next
            target_node.next = new_node
            return

    def remove_node(self, target_node_value) -> None:
        if self.head is None:
            raise EmptyLinkedListException("The Linked list is empty")
        if self.head.data == target_node_value:
            self.head = self.head.next
        previous_node = self.head
        for target_node in self:
            if not target_node.data == target_node_value:
                continue
            previous_node.next = target_node.next
            return



linked_list = LinkedList(nodes=["a", "b", "c", "d"])
# linked_list.add_first_node(Node("primero"))
# linked_list.add_last_node(Node("final"))
# linked_list.insert_after_node("b", "depues_de_b_antes_que_c")
# linked_list.insert_before_node("d", "antes_que_d_despues_que_c")
linked_list.remove_node("a")

print(linked_list)

ll = LinkedList()
ll.add_last_node(Node("primero"))
print(ll)

"""linked_list_elems = [node for node in linked_list]
print(linked_list_elems)
iter_linked_list = iter(linked_list)
next(iter_linked_list)
next(iter_linked_list)"""

"""head_node = Node("0")
linked_list.head = head_node

second_node = Node("1")
head_node.next = second_node

last_node = Node("2")
second_node.next = last_node

print(linked_list)"""
