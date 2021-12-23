import sys

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
        if self.peek == self.limit - 1:
            return True
        return False

    def display(self):
        for item in self.items:
            print(item)

    def num_of_items(self):
        return len(self.items)


def main():
    global stack
    print("Stack")
    print("**********************")
    print("1. create")
    print("2. push")
    print("3. pop")
    print("4. display")
    print("5. Exit")
    while True:
        ch = int(input("enter your choice: "))
        if ch == 1:
            limit = int(input("enter your limit: "))
            stack = Stack(limit)
            print('created successfully')
        elif ch == 2:
            if stack.isFull():
                print('Stack is Full')
                continue
            item = input("enter the item: ")
            stack.push(item)
            print('{} added successfully' .format(item))
        elif ch == 3:
            if stack.isEmpty():
                print('Stack is empty')
                continue
            print('{} is removed successfully'.format(stack.items[stack.peek]))
            stack.pop()
        elif ch == 4:
            print(" items in the stack")
            stack.display()
        elif ch == 5:
            sys.exit()


if __name__ == '__main__':
    main()