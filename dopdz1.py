from collections import deque


class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)
        else:
            raise ValueError("Одна или обе вершины не существуют в графе")

    def print_graph(self):
        for v, neighbors in self.adj_list.items():
            print(f"{v} -> {neighbors}")

    def bfs(self, start_vertex):
        if start_vertex not in self.adj_list:
            raise ValueError("Стартовая вершина отсутствует в графе")

        visited = {start_vertex}
        queue = deque([start_vertex])
        distances = {start_vertex: 0}
        visit_order = []

        while queue:
            curr = queue.popleft()
            visit_order.append(curr)

            for neighbor in self.adj_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)

        return visit_order, distances

    def count_connected_components(self):
        visited = set()
        components_count = 0

        for vertex in self.adj_list:
            if vertex not in visited:
                components_count += 1
                queue = deque([vertex])
                visited.add(vertex)
                while queue:
                    curr = queue.popleft()
                    for neighbor in self.adj_list[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return components_count