def CreateGraph(input_):
    a = input_.split("\n")
    b = []
    for j in a:
        b.append([s for s in re.findall(r"\s*(\d+)\s*", j)])
    for j in b:
        for i, k in enumerate(j):
            if i != 0 and i!=1:
                b.append([j[0], j[i]])
        if len(j) > 2:
            del j[2:]
    new = np.array(sorted(b))
    output = {}
    for j in set(new[:,0]):
        output[j] = [i[1] for i in new[new[:,0]==j,:]]
    return output

CreateGraph(input_)

def FindCycle(start_node, graph):
    cycle = [start_node]
    while True:
        if start_node not in graph:
            return cycle[:-1], graph
        elif len(graph[start_node])>1:
            cycle.append(graph[start_node][0])
            graph[start_node] = graph[start_node][1:]
            start_node = cycle[-1]
        else:
            cycle.append(graph[start_node][0])
            del graph[start_node]
            start_node = cycle[-1]

def FindStartingNode(cycle, graph):
    if bool(cycle):
        for pos,node in enumerate(cycle):
            if node in graph and bool(graph[node]):
                return node, pos
    return list(graph.keys())[0], 0

def EulerianCycle(graph):
    """The graph must be a dictionary of lists"""
    cycle = []
    while bool(set(graph.keys())):
        start_node, pos = FindStartingNode(cycle, graph)
        cycle2, graph = FindCycle(start_node,graph)
        new_cycle = cycle[pos:]
        new_cycle.extend(cycle[:pos])
        new_cycle.extend(cycle2)
        cycle = new_cycle
    cycle.append(new_cycle[0])
    return cycle
