# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def is_symmetric(cls, root: TreeNode) -> bool:
        # 최초 root의 child가 없는 경우 처리
        if root.left is None and root.right is None:
            return True

        left = [root.left]
        right = [root.right]

        # BFS로 구현
        while True:
            # 더 이상 비교해야할 노드가 없다면 종료
            if len(left) == 0 and len(right) == 0:
                break

            cur_left = []
            cur_right = []

            # 탐색해야할 같은 depth의 노드 값 가져오기
            while len(left) >= 1:
                cur_left.append(left.pop(0))

            while len(right) >= 1:
                cur_right.append(right.pop(0))

            # Symmetric => 노드의 갯수는 항상 동일해야함
            if len(cur_left) != len(cur_right):
                return False

            # target 노드들이 같은지 확인
            for idx in range(len(cur_left)):
                pop_l = cur_left.pop(0)
                pop_r = cur_right.pop(0)

                if pop_l is None and pop_r is None:
                    continue
                elif pop_l and pop_r and pop_l.val == pop_r.val:
                    left.append(pop_l.left)
                    left.append(pop_l.right)
                    right.append(pop_r.right)
                    right.append(pop_r.left)
                else:
                    return False

        return True


# Success case
root_case1 = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3)),
)

# Fail case
root_case2 = TreeNode(
    1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3)),
)

print(Solution.is_symmetric(root_case1))
print(Solution.is_symmetric(root_case2))
