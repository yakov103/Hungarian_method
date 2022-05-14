import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

#
# ## bfs dictionary
# def bfs(G, s):
#     """
#     BFS dictionary.
#     """
#     # initialize
#     visited = {}
#     for v in G.nodes():
#         visited[v] = False
#     visited[s] = True
#     # start BFS
#     queue = [s]
#     while queue:
#         v = queue.pop(0)
#         for u in G.neighbors(v):
#             if not visited[u]:
#                 visited[u] = True
#                 queue.append(u)
#     return visited
# ## matching
# def matching(G, s, t):
#     """
#     Maximum matching.
#     """
#     # initialize
#     matching = {}
#     for v in G.nodes():
#         matching[v] = None
#     # start matching
#     while True:
#         # find augmenting path
#         path = bfs(G, matching)
#         if not path:
#             break
#         # augment along path
#         v = path[0]
#         for u in path[1:]:
#             matching[u] = v
#             G.add_edge(u, v)
#     return matching
#
#
# ## hungerian algorithm for maxiumum matching
# def hungarian(G):
#     """
#     Hungarian algorithm for maximum matching.
#     """
#     # initialize
#     matching = {}
#     for v in G.nodes():
#         matching[v] = None
#     # start matching
#     while True:
#         # find augmenting path
#         path = bfs(G, matching)
#         if not path:
#             break
#         # augment along path
#         v = path[0]
#         for u in path[1:]:
#             matching[u] = v
#             G.add_edge(u, v)
#     return matching


if __name__ == '__main__':
    B = nx.Graph()
    B.add_nodes_from([1,2,3,4], bipartite=0)
    B.add_nodes_from(['a','b','c','d','e'], bipartite=1)
    B.add_edges_from([(1,'a'),(1,'b'),(2,'c'),(2,'d'),(3,'b'),(3,'d'),(4,'a'),(4,'c')])

    pos =nx.bipartite_layout(B, [1,2,3,4], align='vertical', scale=2)
    nx.draw_networkx_nodes(B, pos, nodelist=B.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(B, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(B, pos, font_size=16)
    plt.show()

