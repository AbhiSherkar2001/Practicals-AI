Minimum spanning tree
import heapq

# Graph representation using adjacency list
def prim_mst(graph):
    # Number of vertices in graph
    V = len(graph)
    
    # Initialize the priority queue and visited nodes
    min_heap = [(0, 0)]  # (weight, vertex)
    visited = [False] * V
    mst_edges = []
    total_weight = 0
    
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        
        if visited[node]:
            continue
        
        visited[node] = True
        total_weight += weight
        
        # Add the edge to MST (if it's the first edge, it's from the starting node)
        if weight > 0:
            mst_edges.append((node, weight))
        
        # Add all neighbors of the node to the min heap
        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst_edges, total_weight

# Example graph represented as adjacency list [(neighbor, weight)]
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

mst, total_weight = prim_mst(graph)
print("Edges in MST:", mst)
print("Total weight of MST:", total_weight)  

theory
. Greedy Search Algorithm for Minimum Spanning Tree (MST) – Prim’s Algorithm:
Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a graph. It starts with an arbitrary node and grows the MST by adding the least weight edge that connects a node inside the tree to a node outside the tree.

Steps:
Start with an arbitrary node, and mark it as visited.
Add the smallest weight edge that connects a visited node to an unvisited node.
Repeat the above step until all nodes are visited.

Explanation:
Graph Representation: The graph is represented as an adjacency list where each node points to a list of tuples (neighbor, weight).

Priority Queue (Min-Heap): A min-heap (priority queue) is used to pick the smallest edge that connects a visited node to an unvisited node.
Visited Array: Keeps track of visited nodes to prevent cycles.
MST Edges: Stores the edges that are part of the MST.  
