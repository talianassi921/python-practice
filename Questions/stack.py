class Stack(object):
    
    def __init__(self):
        self.object = []
        
    def isEmpty(self, object):
        return self.object == []
    
    def push(self, object):
        """adds an object to the end of the stack"""
        return self.object.append(object)
    
    def pop(self, object):
        """removes an object from the end of the stack"""
        return self.object.pop()
    
    def peek(self, object):
        """peek at the top item"""
        return self.object[len(self.object)-1]
    
    def size(self, object):
        """returns the length of the stack"""
        return len(self.object)
    
stack = Stack()
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.isEmpty)
# print(stack.pop())