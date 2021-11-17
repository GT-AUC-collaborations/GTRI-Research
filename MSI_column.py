import pydot

graphs = pydot.graph_from_dot_file("topic_data.dot")
graph = graphs[0]

print(graph)
