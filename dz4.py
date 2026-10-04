def find_simple_cycles(n, edges, v, K):
    graph = {i: [] for i in range(n)}
    for u, w in edges:
        graph[u].append(w)

    cycles = []

    def dfs(curr, path, length):
        if length > K:
            return
        for neighbor in graph[curr]:
            if neighbor == v and length + 1 <= K:
                cycles.append(path + [v])
            elif neighbor not in path:
                dfs(neighbor, path + [neighbor], length + 1)

    dfs(v, [v], 0)

    unique_cycles = []
    seen = set()
    for cycle in cycles:
        t = tuple(cycle)
        if t not in seen:
            seen.add(t)
            unique_cycles.append(cycle)

    return unique_cycles

n = 4
edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 3)
]
v = 0
K = 4

found_cycles = find_simple_cycles(n, edges, v, K)

print("найденные циклы:")
for c in found_cycles:
    print(c)

print("количество циклов:", len(found_cycles))

print("существует ли цикл:", len(found_cycles) > 0)