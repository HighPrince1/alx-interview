def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Initialize the stack with the first box

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)


# Example cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
