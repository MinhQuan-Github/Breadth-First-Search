import time


def BFS(initialState, goal, graph):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (frontier and explored):
                frontier.append(neighbor)
    return False


if __name__ == '__main__':
    start = time.time()
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [],
        'I': [],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
        'N': [],
        'O': [],
    }

    result = BFS('A', 'O', graph)
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print("404 not found")
    print("cost: ", time.time() - start)
