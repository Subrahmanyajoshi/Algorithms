import sys

sys.path.append('../../')
from data_structures.trees.binary_search_tree import TreeBuilder, Node


class BFSTraversal(object):

    @staticmethod
    def print_bfs(root: Node):
        if root is None:
            return

        height = BFSTraversal.height(root=root)
        if height == 1:
            print(root.value)
            return

        for i in range(1, height+1):
            BFSTraversal.print_current_level(node=root, level=i)

    @staticmethod
    def print_current_level(node: Node, level: int):
        if node is None:
            return

        if level == 1:
            print(node.value)

        elif level > 1:
            BFSTraversal.print_current_level(node=node.left, level=level - 1)
            BFSTraversal.print_current_level(node=node.right, level=level - 1)

    @staticmethod
    def height(root: Node):
        if root is None:
            return 0

        left_height = BFSTraversal.height(root=root.left)
        right_height = BFSTraversal.height(root=root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


if __name__ == '__main__':
    values = [2, 1, 4, 3, 5]

    # Build a binary search tree
    root_node = None
    for value in values:
        root_node = TreeBuilder.build(root=root_node, value=value)

    # Print the newly created binary search tree
    print(root_node)

    # BFS traversal
    BFSTraversal.print_bfs(root=root_node)
