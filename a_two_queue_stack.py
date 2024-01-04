from collections import deque


class MyStack(object):
    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        i = 0
        while i < len(self.q) - 1:
            self.q.append(self.q.popleft())
            i += 1

    def pop(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None

        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None

        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()  # return 2
# obj.pop()
param_3 = obj.top()  # return 1
param_4 = obj.empty()  # Flase
print(param_4)
# 12345

# 43215
# 32154
# 21543
# 15432
# 54321
