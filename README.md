# Work Samples

## Card embeddings -- could not generate access token

In Domo data is visualized through an object called a card, as such there is a lot of value for the Domo product to have autonomous understanding of card objects. One step along this path is to create a low dimensional vector embedding of a high dimensional object (like a card). Think card-to-vec instead of word-to-vec. Card embeddings could have a variety of applications like identifying duplicated visualizations or recommending novel cards to users. For this task you will need to obtain the card data, from this instance, that you will represent by a vector embedding learned via a ML model. You also could demonstrate how well your embedding represents the card object.

## Build an Entity Graph

Given entity types (Users, Cards, Datasets, etc), build a graph that connects all entities from activity data. You can decide what defines a node or an edge, but one example solution is if two entities have an edge connection if the two have interacted in some way. Or in other words, if a user i creates, or saves a card, j, there should be an edge between iÂ and j.Â An entity graph could have a variety of use cases, like identifying the most important entities in this instance.

Completed. Time taken: 3 hrs.