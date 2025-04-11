def find_cheapest_route(routes, src, dst, k):
    # Determine nodes
    nodes = set()
    nodes.add(src)
    nodes.add(dst)
    for route in routes:
        nodes.add(route[0])
        nodes.add(route[1])
    n = len(nodes)  # Number of nodes

    INF = float('inf')  # Represents infinity, used for unreachable nodes

    # Create a mapping from node to index
    node_to_index = {node: i for i, node in enumerate(sorted(list(nodes)))}

    distance = [INF] * n  # Initialize all distances to infinity
    distance[node_to_index[src]] = 0

    # Iterate k+1 times to allow for at most k stops
    for _ in range(k + 1):
        distance_backup = distance.copy()  # Create a copy of the distance from the previous iteratio

        # Iterate through all routes
        for route in routes:
            from_node, to_node, price = route
            from_index = node_to_index[from_node]
            to_index = node_to_index[to_node]
            # Update the distance to the destination if a cheaper route is found
            distance[to_index] = min(distance[to_index], distance_backup[from_index] + price)

    # If distance to destination is still infinity, it's unreachable
    if distance[node_to_index[dst]] == INF:
        return -1
    else:
        return distance[node_to_index[dst]]

if __name__ == "__main__":
    # Test case 1
    routes1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src1 = 0
    dst1 = 2
    k1 = 1
    print(find_cheapest_route(routes1, src1, dst1, k1))  # Expected output: 200
    

    # Test case 2
    routes2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2 = 0
    dst2 = 2
    k2 = 0
    print(find_cheapest_route(routes2, src2, dst2, k2))  # Expected output: 500

    # Test case 3
    routes3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src3 = 0
    dst3 = 3
    k3 = 1
    print(find_cheapest_route(routes3, src3, dst3, k3))  # Expected output: -1
    
    # Test case 4: No routes
    routes4 = []
    src4 = 0
    dst4 = 1
    k4 = 0
    print(find_cheapest_route(routes4, src4, dst4, k4))  # Expected output: -1