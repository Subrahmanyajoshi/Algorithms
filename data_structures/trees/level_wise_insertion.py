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

        new_node = TreeBuilder.create_node(data=value)
        if root is None:
            return new_node

        q = [root]

        while q:
            node = q.pop(0)

            if node.left is None:
                node.left = new_node
                break
            else:
                q.append(node.left)

            if node.right is None:
                node.right = new_node
                break
            else:
                q.append(node.right)
        return root


if __name__ == '__main__':
    values = [1, 3, 5, 6, 2, 7, 8, None, 1]

    root = None
    for value in values:
        root = TreeBuilder.build(root=root, value=value)
    print(root)
