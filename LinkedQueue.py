from AbstractCollection import AbstractCollection
from Node import Node

class LinkedQueue(AbstractCollection):

    """Linked-list based implementation of queue"""
    def __init__(self):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self)

    def add(self,item):
        new_node = Node(item)

        if self.is_empty():
            """No nodes in the linked list """
            self._front = new_node
            self._rear = new_node
        else:
            """At least one node in the linked list"""
            self._rear._next = new_node
            self._rear = new_node
        self._size +=1

    def pop(self):
        """
        Precondition: Queue is not empty
        Raises: ValueError if queue is empty
        Postcondition: Queue has one less item in it
        :return: item at the front of the queue
        """
        if self.is_empty():
            raise ValueError("Cannot pop an empty queue!")
        return_item = self._front._data
        self._front = self._front._next

        if self._front is None:
            """Queue only had 1 item in it"""
            self._rear = None

        self._size -=1
        return return_item

    def clear(self):
        """Makes self empty"""
        self._front = None
        self._rear = None
        self._size = 0
    def peek(self):
        """Returns the entry at the front of the queue
        Precondition: queue is not empty
        Raises: ValueError if the queue is empty
        """
        if self.is_empty():
            raise ValueError("Can't peek an empty queue")
        return self._front._data


    def __str__(self):
        """Testing purposes only """
        return_string = ""
        probe = self._front
        while probe is not None:
            return_string += " " + str(probe._data)
            probe = probe._next

        return return_string




