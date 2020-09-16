from collections import deque


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]


def color_graph(graph, colors):
    # this solution has O(N+M) runtime complexity
    # but O(N) space. InterviewCake's solution is O(D) space,
    # with D number of colors.

    # The problem with my solution is that I am using BFS to explore the graph,
    # even though we know everything about it already. Using that information
    # can save us some pùspace complexity: iterating over the graph list we
    # would only need to store the neighbours colors to avoid them.

    visited_nodes = set()

    while len(visited_nodes) != len(graph):
        queue = deque()
        for i in range(len(graph)):
            if graph[i] not in visited_nodes:
                queue.append(graph[i])

        while len(queue):
            node = queue.popleft()
            visited_nodes.add(node)

            possible_colors = [color for color in colors]

            for neighbor in node.neighbors:
                if neighbor == node:
                    raise Exception('It is not possible to legally color a graph with loops')

                if neighbor.color in possible_colors:
                    possible_colors.remove(neighbor.color)
                if neighbor not in visited_nodes and neighbor not in queue:
                    queue.append(neighbor)
            node.color = possible_colors.pop()
    return 0
