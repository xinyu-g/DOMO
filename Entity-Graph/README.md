# Build an Entity Graph

Given entity types (Users, Cards, Datasets, etc), build a graph that connects all entities from activity data. You can decide what defines a node or an edge, but one example solution is if two entities have an edge connection if the two have interacted in some way. Or in other words, if a user i creates, or saves a card, j, there should be an edge between iÂ and j.Â An entity graph could have a variety of use cases, like identifying the most important entities in this instance.


## Data Exploration 

(You can follow the exploration steps in the jupyter notebook)

Given that I have no prior knowledge about the data, except for the column names and types, I intend to execute some basic commands on the data to gain more insights. I have a few questions in mind that will guide my exploration:

1. What is the meaning of each column?
2. Which columns correspond to entity types?
3. For each entry, what activity does it signify? Is it the initiator, recipient, or something else?

Upon delving deeper into the data, and gaining a better grasp of the significance of each column and the distinct values it contains, it appears that the "Object_Type" and "Type" columns are the most probable sources of information regarding entity types. My next objective is to determine which columns, when used in combination, would provide me with the most comprehensive information about the initiator and recipient of an activity.

Based on my further analysis, I have formulated a hypothesis that for each entry, the "Name" column corresponds to the name of the initiator, the "Type" column corresponds to the entity type of the initiator, the "Action" column corresponds to the action of the initiator, the "Object_Name" column corresponds to the name of the action receiver, and the "Object_Type" column corresponds to the entity type of the receiver. My strategy to identify the types of entities that interact with each other involves grouping the data based on "Object_Type" and "Type". 

Having obtained the unique pairs, I can now proceed with constructing an entity graph. I will consider each unique instance in the set comprising "Object_Type" and "Type" as a node in the graph. For each pair of "Type" and "Object_Type", I will create a directed edge between them, with the count of such pairs serving as the weight of the corresponding edge.


### Data Structure

I have created a "Vertex" class and a "Graph" class to serve as the foundation for the graph structure. Each vertex contains information on its neighboring vertices and the weight of the corresponding edges. For a more comprehensive understanding of these implementations, please refer to the "graph.py" file.


### Deliverables

`pip install -r requirements.txt`

Execute the file graph.py

`python graph.py`

The program will display a printout of all edges contained within the final graph. Furthermore, it will generate two image files, each of which depicts the graph in a distinct layout.
