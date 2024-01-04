class MyQueue(object):
    def __init__(self):
        self.in_s = []
        self.out_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_s.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.out_s.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_s:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
        return self.out_s[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_s and not self.out_s


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)  # in: 1234 / out: x
obj.pop()  # in: x / out: 432 / result: 1
obj.push(5)  # in: 5 / out: 432
obj.pop()  # in: 5 / out: 43 / result: 2
obj.pop()  # in: 5 / out: 4 / result: 3
obj.pop()  # in: 5 / out: x / result: 4
obj.pop()  # in: x / out: x / result: 5
print(obj.empty())  # result: true
