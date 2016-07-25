import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class TreeHeight:
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
            self.height = [0] * self.n

        def compute_height(self):
            max_height = 0

            for vertex in range(self.n):
                max_height = max(max_height, self.height_to_node(vertex))

            return max_height

        def height_to_node(self, node):
            if node == -1:
                return 0
            if self.height[node] != 0:
                return self.height[node]

            self.height[node] = 1 + self.height_to_node(self.parent[node])

            return self.height[node]


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
