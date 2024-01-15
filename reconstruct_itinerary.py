import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 그래프 구성(어휘순)
        graph = collections.defaultdict(list)
        for depart, arrival in sorted(tickets):
            graph[depart].append(arrival)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        # "JFK"에서 출발하는 여행 일정 구성하기
        dfs("JFK")
        # 다시 뒤집어야 원하는 결과 나옴
        return route[::-1]


s = Solution()
print(
    s.findItinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    )
)
