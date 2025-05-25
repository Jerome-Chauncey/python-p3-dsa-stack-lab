class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1
    

# stack = Stack(limit=4)

# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)

# print("Current stack items:", stack.items)
# print("Top of stack:", stack.peek())
# print("Stack size:", stack.size())
# print("Is the stack full?", stack.full())
# print("Is the stack empty?", stack.isEmpty())
# print("Search 300", stack.search(300))

# for item in stack.items:
#     print(item)
