from collections import deque


# bfs
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 각 과목을 선수 과목으로 하는 후수 과목들의 리스트
        latter_courses = [[] for _ in range(numCourses)]
        # indegree: 특정 노드에 대해서 다른 노드로부터 들어오는 간선의 개수. 여기서는 각 과목의 선수 과목 수.
        indegree = [0] * numCourses

        # a: 후수 과목 b: 선수 과목
        for a, b in prerequisites:
            latter_courses[b].append(a)
            indegree[a] += 1

        # 선수 과목 없이 바로 수강 가능한 과목들을 큐에 추가
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            # 현재 수강할 과목 꺼내기
            curr = q.popleft()
            for latter_course in latter_courses[curr]:
                # 현재 과목을 수강한다면 후수 과목을 수강할 수 있는 조건이 하나 충족됨
                indegree[latter_course] -= 1
                # 모든 선수 과목을 수강한 상태이면 큐에 추가
                if indegree[latter_course] == 0:
                    q.append(latter_course)
            # 하나의 과목을 수강했으므로 남은 과목 수 1 감소
            numCourses -= 1

        # 모든 과목을 수강했다면 True, 아직 수강하지 않은 과목이 남아 있다면 False
        return numCourses == 0
