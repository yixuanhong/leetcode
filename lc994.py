class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: 找到所有 rotten oranges, 并统计 fresh oranges 数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # 如果没有 fresh，直接 0 分钟
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS 扩散腐烂
        while queue:
            size = len(queue)
            spread = False  # 记录这一分钟有没有腐烂
            
            for _ in range(size):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2   # 腐烂
                        fresh -= 1
                        spread = True
                        queue.append((nx, ny))
            
            if spread:
                minutes += 1
        
        return minutes if fresh == 0 else -1
