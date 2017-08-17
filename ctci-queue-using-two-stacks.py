# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/

class MyQueue(object):
    def __init__(self):
        self.first = list()
        self.second = list()
    
    def __prep__(self):
        if len(self.second) == 0:
            while len(self.first) > 0:
                self.second.append(self.first.pop())
    
    def peek(self):
        self.__prep__()
        return self.second[-1]
        
    def pop(self):
        self.__prep__()
        return self.second.pop()
        
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
