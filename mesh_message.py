network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott'],
    'Scott': [],
    'Sofia': []
}


def process_path(parents, start, end):
    current = end
    path = []
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()
    return path


def get_path(network, start, end):
    # iterative BFS to find path to end from start
    if start not in network:
        raise Exception('Start node not in graph')
    if end not in network:
        raise Exception('End node not in graph')
    queue = [start]
    i = 0
    visited = set()
    parents = {start: None}
    while i < len(queue):
        node_name = queue[i]
        visited.add(node_name)
        i += 1
        if node_name == end:
            return process_path(parents, start, end)
        neighbours = network[node_name]
        for neighbour in neighbours:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
                parents[neighbour] = node_name
    return None


print(get_path(network, 'Min', 'Noam'))
