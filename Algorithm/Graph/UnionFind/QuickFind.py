class QuickFind:
    def __init__(self, size: int):
        """UnionFind Array version initiation"""
        self.root = [idx for idx in range(size)]

    def find(self, root_val: int):
        """Find root value of element"""
        return self.root[root_val]

    def union(self, x: int, y: int):
        """union slow version"""
        root_x = self.root[x]
        root_y = self.root[y]

        if root_x != root_y:
            for idx in range(len(self.root)):
                if self.root[idx] == root_y:
                    self.root[idx] = root_x

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


# Test section
union_find = QuickFind(10)
print(union_find.root)

# [0, 1, 2, 3, 4, 5, 6, 7 ...]
union_find.union(0, 2)
union_find.union(0, 3)
print(union_find.root)

union_find.union(5, 6)
union_find.union(5, 7)
print(union_find.root)

assert union_find.connected(0, 3)
assert not union_find.connected(0, 1)
