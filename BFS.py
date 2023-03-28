graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '4' : ['6'],
  '5' : [],
  '3' : ['7'],
  '6' : [],
  '7' : []
}
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("Following is the Breadth-First Search")
bfs(visited, graph, '1')    # function calling
