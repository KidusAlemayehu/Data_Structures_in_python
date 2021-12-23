class Stack:
    def __init__(self, limit):
        self.items = []
        self.peek = -1
        self.limit = limit
        
    def push(self, item):
        self.peek += 1
        return self.items.append(item)
    
    def pop(self):
        self.peek += 1
        return self.items.pop()

    def isEmpty(self):
        if self.peek == -1:
            return True
        return False

    def isFull(self):
        if self.peek == self.limit:
            return True
        return False

    def display(self):
        for item in self.items:
            print(item)
