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
    def create_node(data):
        node = Node(value=data)
        node.left = node.right = None
        return node

    @staticmethod
    def build(root: Optional[Node], value: int):

        if root is None:
            root = TreeBuilder.create_node(data=value)
            return root

        if value < root.value:
            root.left = TreeBuilder.build(root=root.left, value=value)
        else:
            root.right = TreeBuilder.build(root=root.right, value=value)

        return root


if __name__ == '__main__':
    values = [1, 3, 5, 6, 2]

    root = None
    for value in values:
        root = TreeBuilder.build(root=root, value=value)

    print(root)
