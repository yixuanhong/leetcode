class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        
        # 图的邻接表
        graph = defaultdict(list)
        # 入度
        indegree = [0] * numCourses
        
        # 构建图
        for a, b in prerequisites:  # b -> a
            graph[b].append(a)
            indegree[a] += 1
        
        # queue 放所有入度为 0 的课程
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        
        while queue:
            course = queue.popleft()
            res.append(course)
            
            # 遍历它指向的课程
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        # 如果能排完，res 长度 = numCourses
        return res if len(res) == numCourses else []
