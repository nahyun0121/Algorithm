# 개별 체이닝 방법으로 구현
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(
            ListNode
        )  # 각 ListNode를 담게 될 기본 자료형 선언. collections.defaultdict: 키 조회 시 자동으로 디폴트를 생성해줌

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우(해시 충돌) 연결 리스트 처리
        p = self.table[index]  # 인덱스의 첫 번째 값(노드)
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            # p가 마지막 노드라면, 빈 ListNode 객체 할당 / p 뒤에 다른 노드가 있다면, p 노드를 삭제하고 그 다음 노드를 첫 번째 노드로 만듦
            # 빈 ListNode 할당하는 이유: self.table은 defaultdict(ListNode)이므로 매번 빈 노드를 생성함.
            # None 할당하면 추가, 조회 함수에서 비교 구문 에러 발생
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
