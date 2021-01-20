# Algorithm
# bfs(graph):
#   while all vertices are not explored:
#     enque(any vertex) to queue q
#     while q is not empty:
#       p=dequeue()
#       if p is unvisited:
#         print(p)
#         mark p as visited
#         enqueue(all adjecent nodes of p)

# in disconnected graph we can't performe bfs or dfs.
# time complexcity=v+e
# space complexcity=v+e
