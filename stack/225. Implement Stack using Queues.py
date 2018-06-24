from collections import deque


class MyStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for _ in range(0, len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
