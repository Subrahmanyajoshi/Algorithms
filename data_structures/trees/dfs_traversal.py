import sys

sys.path.append('../../')
from data_structures.trees.binary_search_tree import TreeBuilder, Node


class DFSTraversal(object):

    @staticmethod
    def in_order(root: Node):

        if root is None:
            return

        DFSTraversal.in_order(root=root.left)
        print(root.value)
        DFSTraversal.in_order(root=root.right)

    @staticmethod
    def pre_order(root: Node):

        if root is None:
            return

        print(root.value)
        DFSTraversal.pre_order(root=root.left)
        DFSTraversal.pre_order(root=root.right)

    @staticmethod
    def post_order(root: Node):
        if root is None:
            return

        DFSTraversal.post_order(root=root.left)
        DFSTraversal.post_order(root=root.right)
        print(root.value)


if __name__ == '__main__':
    values = [2, 1, 4, 3, 5]

    # Build a binary search tree
    root_node = None
    for value in values:
        root_node = TreeBuilder.build(root=root_node, value=value)

    # Print the newly created binary search tree
    print(root_node)

    # DFS traversal can be done in 3 ways
    print("Inorder")
    DFSTraversal.in_order(root=root_node)

    print("Preorder")
    DFSTraversal.pre_order(root=root_node)

    print("Postorder")
    DFSTraversal.post_order(root=root_node)
