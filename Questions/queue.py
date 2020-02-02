class Queue(object):
    
    def __init__(self):
        self.object = []
        
    def isEmpty(self, object):
        return self.object == []
    
    def push(self, object):
        """adds an object to the end of the queue"""
        return self.object.append(object)
    
    def pop(self, object):
        """removes an object from the front of the queue"""
        return self.object.pop(0)
    
    def peek(self, object):
        """peek at the top item"""
        return self.object[len(self.object)-1]
    
    def size(self, object):
        """returns the length of the queue"""
        return len(self.object)
    