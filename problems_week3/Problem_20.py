def CreateGraph(input_):
    kmers = input_.split("\n")
    graph = {}
    for kmer in kmers:
        graph.setdefault(kmer[:-1],[]).append(kmer[1:])
    return graph

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

def ReorganizeCycle(cycle,cycle2,pos):
    new_cycle = cycle[pos:]
    new_cycle.extend(cycle[:pos])
    new_cycle.extend(cycle2)
    return new_cycle

def EulerianCycle(graph):
    """The graph must be a dictionary of lists"""
    cycle = []
    while bool(set(graph.keys())):
        start_node, pos = FindStartingNode(cycle, graph)
        cycle2, graph = FindCycle(start_node,graph)
        cycle = ReorganizeCycle(cycle,cycle2,pos)
    end_node = cycle[0]
    cycle.append(end_node)
    return cycle

def FindSemiBalancedNodes(graph):
    count_edges = {}
    values = []
    for values_list in graph.values():
        values.extend(values_list)
    values.extend(graph.keys())
    values = set(values)
    for node in values:
        if node in graph:
            out_edges = len(graph[node])
        else:
            out_edges = 0
        in_edges = sum([1 for n in graph if node in graph[n]])
        count_edges[node] = (out_edges,in_edges)
    return [(node,count_edges[node][0]-count_edges[node][1]) for node in count_edges
            if count_edges[node][0]-count_edges[node][1] !=0]

def EulerianPath(graph):
    semi_balanced = FindSemiBalancedNodes(graph)
    for node,i in semi_balanced:
        if i>0:
            node_in = node
        else:
            node_out = node
    graph.setdefault(node_out,[]).append(node_in)
    cycle = EulerianCycle(graph)
    new_cycle = []
    for i,node in enumerate(cycle):
        if node == node_out and cycle[i+1] == node_in:
            new_cycle = cycle[i+1:]
            new_cycle.extend(cycle[1:i+1])
    return new_cycle

def ReconstructStringFromGenomePath(text):
    output = text[0]
    for word in text[1:]:
        output = output + word[-1]
    return output

def StringFromComposition(graph):
    path = EulerianPath(graph)
    return ReconstructStringFromGenomePath(path)
