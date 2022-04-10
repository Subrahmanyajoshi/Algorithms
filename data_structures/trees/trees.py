from typing import Optional


class Node(object):

    def __init__(self, value):
        self.value = value
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None

    def __str__(self, level=0):
        ret = "  " * level + f"- {self.value}\n"
        if self.left is not None:
            ret += self.left.__str__(level + 1)
        if self.right is not None:
            ret += self.right.__str__(level + 1)
        return ret


# A basic tree data structure builder
class TreeBuilder(object):

    @staticmethod
    def build():
        root_node = Node("Root")
        root_node.left = Node("Left child")
        root_node.right = Node("Right child")
        return root_node


if __name__ == '__main__':
    print(TreeBuilder.build())
