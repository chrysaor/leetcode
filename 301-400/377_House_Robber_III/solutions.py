from typing import Optional, Tuple


# 트리 노드 클래스
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def search_node(node) -> Tuple[int, int]:
            """
            해당 노드에서 훔칠 수 있는 최대 값을 가져온다.
            Args:
                node (TreeNode): 트리 노드 값

            Returns:
                Tuple[int, int]: [털었을때 최대 값, 안털었을때 최대 값]
            """
            # 빈 노드인 경우 (0, 0) 반환
            if not node:
                return 0, 0

            left = search_node(node.left)
            right = search_node(node.right)

            # 첫 리프노드까지 도달시 리프노드 값 + 0 + 0 => 리프노드값 반환
            # 결과적으로 지금 노드의 값 + 각 자식 노드별 최대값의 합
            rob = node.val + left[1] + right[1]

            # 안터는 경우 각 자식 노드별 최대값의 합
            not_rob = max(left) + max(right)

            return rob, not_rob

        return max(search_node(root))

    @classmethod
    def dfs_solution(cls, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # DFS 버전
            if not node:
                return 0, 0

            # One line 호출로 현재 Depths 값들 동시 참조 가능
            l, r = dfs(node.left), dfs(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]

        return max(dfs(root))
