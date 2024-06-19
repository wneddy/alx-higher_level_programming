#!/usr/bin/python3
"""singly linked lists"""


class Node:
    """class node declared"""
    
    def __init__(self, data, next_node=None):
        """initializing instances.

        Args:
            data (int): data to be stored.
            next_node: next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retreive data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setting value to data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieving next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setting up next node to value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """declaration of the list class"""

    def __init__(self):
        """ simple initialization"""
        self.head = None

    def sorted_insert(self, value):
        """method to insert node"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """method to append data to the list."""
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

