class UnionByRank:
    def __init__(self, size: int):
        """UnionFind Array version initiation"""
        self.root = [idx for idx in range(size)]
        self.rank = [1] * size

    def find(self, x: int):
        """Find root value of element"""
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        """union fast version"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


# Test section
union_find = UnionByRank(10)
print(union_find.root)
print(union_find.rank)
print("")

# [0, 1, 2, 3, 4, 5, 6, 7 ...]
union_find.union(0, 2)
union_find.union(0, 3)
print(union_find.root)
print(union_find.rank)
print("")

union_find.union(5, 6)
union_find.union(5, 7)
print(union_find.root)
print(union_find.rank)
print("")

assert union_find.connected(0, 3)
assert not union_find.connected(0, 1)
