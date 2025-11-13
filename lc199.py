class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # 最右边的就是每层的最后一个 (i == level_size - 1)
                if i == level_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
