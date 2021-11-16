import queue
from timeit import default_timer as timer

'''
assumptions:
- directed simple graph
- nodes have unique ids
'''

def timeit(fn):
    def wrapper(*args, **kwargs):
        start = timer()
        x = fn(*args, **kwargs)
        elapsed = timer() - start
        print(f'{elapsed * 1000} ms')
        return x
    return wrapper

class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = []
        self.marked = False

@timeit
def search(graph, startId, endId):
    q = queue.SimpleQueue()
    start = graph[startId]
    end = graph[endId]
    start.marked = True
    q.put(start)

    while not q.empty():
        curr = q.get()

        if curr.id == end.id:
            return True

        for nodeId in curr.adjacent:
            node = graph[nodeId]

            if not node.marked:
                node.marked = True
                q.put(node)

    return False

'''
case 1

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
'''
case1 = [Node(i) for i in range(0, 9)]

for i in range(0, len(case1) - 1):
    case1[i].adjacent.append(i + 1)

'''
case 2

0 -> 1 -> 2 -> 3
4 -> 5 -> 6 -> 7 -> 8
'''
case2 = [Node(i) for i in range(0, 9)]

for i in range(0, 3):
    case2[i].adjacent.append(i + 1)

for i in range(4, len(case2) - 1):
    case2[i].adjacent.append(i + 1)

if __name__ == "__main__":
    print(search(case1, 0, 8))   # True
    print(search(case2, 0, 8))   # False        