# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def pre_order(self, node):
        if not node: return
        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def pre_order_(self, node):
        nodes = []

        while node or nodes:
            while node:
                print(node.data, end=" ")
                nodes.append(node)
                node = node.left
            node = nodes.pop()
            node = node.right

    def mid_order(self, node):
        if not node: return
        self.mid_order(node.left)
        print(node.data, end=" ")
        self.mid_order(node.right)

    def mid_oder_(self, node):
        nodes = []
        while node or nodes:
            while node:
                nodes.append(node)
                node = node.left
            node = nodes.pop()
            print(node.data, end=" ")
            node = node.right

    def las_order(self, node):
        if not node: return
        self.las_order(node.left)
        self.las_order(node.right)
        print(node.data, end=" ")

    def las_order_(self, node):
        pre = node
        nodes = []
        while node or nodes:
            while node:
                nodes.append(node)
                node = node.left

            node = nodes[-1].right
            if not node or node is pre:
                node = nodes.pop()
                print(node.data, end=" ")
                pre = node
                node = None

    def bfs(self, node):
        nodes = [node]
        while nodes:
            cur = nodes.pop(0)
            print(cur.data, end=" ")
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)

    def dfs(self, node):
        if not node:return
        print(node.data, end=" ")
        self.dfs(node.left)
        self.dfs(node.right)

    def max_deepth(self, node):
        if not node:return 0
        return max(self.max_deepth(node.left), self.max_deepth(node.right))+1

if __name__ == '__main__':
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    t = Tree()
    print("先序遍历")
    t.pre_order(tree)
    print()
    t.pre_order_(tree)
    print("\n中序遍历")
    t.mid_order(tree)
    print()
    t.mid_oder_(tree)
    print("\n后序遍历")
    t.las_order(tree)
    print()
    t.las_order_(tree)
    print("\n广度遍历")
    t.bfs(tree)
    print("\n深度遍历")
    t.dfs(tree)
    print("\n树的深度")
    print(t.max_deepth(tree))
