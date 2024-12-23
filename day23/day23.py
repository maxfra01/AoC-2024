data = open('input.txt').readlines()
data = [x.strip() for x in data]

connections = []

for line in data:
    line = line.split('-')
    connections.append((line[0], line[1]))

network = {}
for a, b in connections:
    if a not in network:
        network[a] = set()
    if b not in network:
        network[b] = set()
    network[a].add(b)
    network[b].add(a)

triangles = set()
for a in network:
    for b in network[a]:
        for c in network[a]:
            if b != c and b in network and c in network[b]:
                triangles.add(tuple(sorted([a, b, c])))

filtered_triangles = [triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)]
print(len(filtered_triangles))


def find_largest_clique(network):
    max_clique = set()
    for node in network:
        clique = set([node])
        for neighbor in network[node]:
            if all(neighbor in network[other] for other in clique):
                clique.add(neighbor)
        if len(clique) > len(max_clique):
            max_clique = clique
    return max_clique

largest_clique = find_largest_clique(network)

password = ','.join(sorted(largest_clique))
print(password)


