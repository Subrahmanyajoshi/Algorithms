from typing import List


class Node(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):

    def __init__(self, head: Node):
        self.head_ptr = head
        self.last_ptr = self.head_ptr

    def __str__(self):
        print_ptr = self.head_ptr.next
        print_str = ""
        while print_ptr:
            if print_ptr.next:
                print_str += f"{print_ptr.val} -> "
            else:
                print_str += f"{print_ptr.val}"
            print_ptr = print_ptr.next
        return print_str

    def insert(self, values):
        values = [values] if not isinstance(values, List) else values
        for value in values:
            self.last_ptr.next = Node(val=value)
            self.last_ptr = self.last_ptr.next

    def delete(self, n: int):
        location_ptr = self.head_ptr
        for _ in range(n - 1):
            if location_ptr.next is None:
                raise ValueError("Invalid location number for the given linked list")
            location_ptr = location_ptr.next

        del_ptr = location_ptr.next
        location_ptr.next = location_ptr.next.next
        del del_ptr


def main():
    linked_list = LinkedList(head=Node())
    linked_list.insert(values=[1, 2, 4, 2, 2, 5])
    print(linked_list)

    linked_list.delete(3)
    print(linked_list)


if __name__ == '__main__':
    main()
