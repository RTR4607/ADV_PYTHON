class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

#obj.peek()
print(obj.peek())
