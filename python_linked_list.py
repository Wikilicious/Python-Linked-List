__author__ = 'Thomaz L Santana'


class LinkedList(object):
    """ Linked List.
    """
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return str(self.value)

    def insert(self, value):
        """ O(1)
        """
        if self.head is None:
            self.head = self.Node(value)
        else:
            new = self.Node(value)
            new.next = self.head
            self.head = new

    def append(self, value):
        """ O(n)
        """
        if self.head is None:
            self.head = self.Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            new = self.Node(value)
            node.next = new

    def get_all(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_all_raw(self):
        node = self.head
        node_list = []
        while node is not None:
            node_list.append(node)
            node = node.next
        return node_list

    def reverse(self):
        temp_head = self.head.next
        self.head.next = None
        while temp_head is not None:
            temp_next = temp_head.next
            temp_head.next = self.head
            self.head = temp_head
            temp_head = temp_next

    def __delete(self, value, **kwargs):
        if self.head is not None:
            del_all = kwargs.pop('del_all', True)
            node = self.head
            one_deleted = False
            while node.next is not None:
                if node.next.value == value:
                    one_deleted = True
                    node.next = node.next.next
                    if not del_all:
                        break
                else:
                    node = node.next
            if del_all or not one_deleted:
                if self.head.value == value:
                    self.head = self.head.next

    def delete(self, *args):
        if len(args) == 0:
            self.head = self.head.next
        else:
            for value in args:
                self.__delete(value)

    def delete_one(self, value):
        self.__delete(value, del_all=False)

    def swap(self, x, y):
        if x == y:
            pass
        if x > y:
            temp = x
            x = y
            y = temp
        node = self.head
        i = 1
        pre_x = None
        pre_y = None
        while node.next is not None:
            if i == x:
                pre_x = node
            if i == y:
                pre_y = node
            node = node.next
            i += 1
        if pre_x is not None and pre_y is not None and y - x > 1:
            post_y = pre_y.next.next
            post_x = pre_x.next.next
            temp_x = pre_x.next
            pre_x.next = pre_y.next
            pre_x.next.next = post_x
            pre_y.next = temp_x
            pre_y.next.next = post_y
        elif pre_x is not None and pre_y is not None:
            temp_x = pre_x.next
            post_y = pre_y.next.next
            pre_x.next = pre_x.next.next
            pre_x.next.next = temp_x
            temp_x.next = post_y
        elif x == 0 and pre_y is not None and y - x > 1:
            post_y = pre_y.next.next # next nodes of x & y
            post_x = self.head.next
            temp_x = self.head # pointer to x
            self.head = pre_y.next # assign x pointer to y
            self.head.next = post_x # assign next to new x
            pre_y.next = temp_x # assign y pointer to x
            pre_y.next.next = post_y # assign next to new y
        elif x == 0 and pre_y is not None:
            # pointer to X
            temp_x = self.head
            post_y = self.head.next.next
            self.head = self.head.next
            self.head.next = temp_x
            temp_x.next = post_y

    def bubble_sort(self):
        # todo write new swap method to take in two objects to swap instead of index. Currently it's ~O(n^3)
        no_swap = True
        while no_swap:
            no_swap = False
            node = self.head
            i = 0
            while node.next is not None:
                if node.value > node.next.value:
                    self.swap(i, i + 1)
                    no_swap = True
                else:
                    node = node.next
                i += 1
