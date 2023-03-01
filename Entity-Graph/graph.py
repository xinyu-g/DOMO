import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id)

    # add edge from self to neighbor
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    # get all connected entities
    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    # get the weight of an edge 
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()
    

if __name__ == "__main__":

    entity_graph = Graph()

    data = pd.read_csv('./Dataset Activity.csv', dtype={
        'Object_Name': str,
        'User_ID': str,
        'Source_ID': str,
        'Name': str,
        'Action': str,
        'Object_Type': str,
        'Object_ID': str,
        'Type': str,
        'Event_Time': str,
        'Device': str,
        'Browser_Details': str
    })

    # obtain the set of unique entity types 
    vertices = set().union(data['Type'].unique(), data['Object_Type'].unique())

    population = {}

    # create vertices in the graph
    for v in vertices:
        entity_graph.add_vertex(v)
        population[v] = data[data['Type']==v]['Type'].count() + data[data['Object_Type']==v]['Object_Type'].count()


    edata = data.groupby(['Type', 'Object_Type']).size().reset_index().rename(columns={0:'count'})

    edata.sort_values('count', inplace=True)

    edges = edata.values 

    file = open('edges.txt', 'w')

    for u,v,w in edges:
        entity_graph.add_edge(u,v,w)
        file.write(u + ' ' + v + ' ' + str(w) + '\n')
    
    file.close()

    

    # print the edges
    for vertex, edges in entity_graph.vert_dict.items():
        
        for u, w in edges.adjacent.items():
            print(vertex, '->', u, w)


    # plot the graph using networkx

    G = nx.read_weighted_edgelist('edges.txt', delimiter=" ")

    for i in list(G.nodes()):
        G.nodes[i]['population'] = population[i] 
        

    plt.figure()
    node_color = [G.degree(v) for v in G]
    node_size = [0.001 * nx.get_node_attributes(G, 'population')[v] for v in G]
    edge_width = [0.000015 * G[u][v]['weight'] + 0.3 for u, v in G.edges()]

    pos = nx.shell_layout(G)

    nx.draw_networkx(G, pos, node_size = node_size, 
                 node_color = node_color, alpha = 0.7,
                 with_labels = True, width = edge_width,
                 edge_color ='.4', font_size=5)
    
    plt.tight_layout()
    
    plt.savefig('Entity_Graph_shell.png')

    plt.clf()

    pos = nx.circular_layout(G)

    nx.draw_networkx(G, pos, node_size = node_size, 
                 node_color = node_color, alpha = 0.7,
                 with_labels = True, width = edge_width,
                 edge_color ='.4', font_size=5)
  
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('Entity_Graph_circle.jpg')
