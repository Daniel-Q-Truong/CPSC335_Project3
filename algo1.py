from collections import deque

def min_days_to_burn(forest):
    if not forest:
        return -1

    rows, cols = len(forest), len(forest[0])
    queue = deque()
    healthy_trees = 0
    days = 0

    # Step 1: Collect burned trees and count healthy trees
    for r in range(rows):
        for c in range(cols):
            if forest[r][c] == 2:
                queue.append((r, c))
            elif forest[r][c] == 1:
                healthy_trees += 1

    if healthy_trees == 0:
        return days
    if not queue:
        return -1

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Step 2: BFS
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and forest[nr][nc] == 1:
                    forest[nr][nc] = 2
                    healthy_trees -= 1
                    queue.append((nr, nc))
        if queue:
            days += 1

    return days if healthy_trees == 0 else -1

forest1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print("Sample 1: " + str(forest1))
print("Output:" + str(min_days_to_burn(forest1)) )  # Output: 4

forest2 = [
    [2,1,1],
    [0,1,1],
    [1,0,0]
]
print("Sample 2: " + str(forest2))
print("Output:" + str(min_days_to_burn(forest2)) )  # Output: -1

forest3 = [
    [0,2]
]
print("Sample 3: " + str(forest3))
print("Output:" + str(min_days_to_burn(forest3)) )   # Output: 0

forest4 = [
    [1,1,1,2],
    [1,2,0,1],
    [1,1,0,1]
]
print("Sample 4: " + str(forest4))
print("Output:" + str(min_days_to_burn(forest4)) )   # Output: 2
