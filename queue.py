def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    return queue.pop(0)

my_queue = []

enqueue(my_queue, "a")
enqueue(my_queue, "b")
enqueue(my_queue, "c")

print(my_queue)

print(dequeue(my_queue))

print(my_queue)
