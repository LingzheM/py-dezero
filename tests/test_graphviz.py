from graphviz import Digraph

dot = Digraph(comment='Simple Graph')

dot.node('A', 'Node A')
dot.node('B', 'Node B')

dot.edge('A', 'B', label='connect to')

print(dot.source)

dot.render(filename='simple_graph', view=True)