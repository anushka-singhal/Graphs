def add_node(v):
    global node_count
    if v in nodes:
        print("present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print("not present")
    elif v2 not in nodes:
        print("not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost
        
def delete_node(v):
    global node_count
    if v not in nodes:
        print("not present")
    else:
        index1 = nodes.index(v)
        nodes_count = node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()
        
nodes = []
graph = []
node_count = 0
print("before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("N")
add_edge("A","N",10)
delete_node("A")
print("after adding")
print(nodes)
print(graph) 
print_graph()
