import queue
q=queue.Queue()
q.put((2,10))
q.put((1,20))
q.put((4,30))
q.put((3,40))
while not q.empty():
    print(q.get(),end=' ')