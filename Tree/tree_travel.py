
def dfs(graph, node, visited):
  visited[node] = True
  for neighbor in graph[node]:
    if not visited[neighbor]:
      dfs(graph, neighbor, visited)

def main():
  n, e = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

  visited = [False] * (n + 1)
  count = 0
  for i in range(1, n + 1):
    if not visited[i]:
      count += 1
      dfs(graph, i, visited)

  print("conunt:")
  print(count)

if __name__ == "__main__":
  main()
