
# Open the input file in read mode
with open('graph_input.txt', 'r') as file:
    num_nodes = int(file.readline().strip())  # Read the number of nodes
    adj_matrix = []

    # Read the adjacency matrix rows
    for _ in range(num_nodes):
        row = list(map(int, file.readline().strip().split()))
        adj_matrix.append(row)

# Display the adjacency matrix
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
