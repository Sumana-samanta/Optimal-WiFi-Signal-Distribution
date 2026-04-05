# A* Pathfinder for WiFi Signal Optimization

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position


def astar(start, end, grid):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []
    open_list.append(start_node)

    while open_list:
        # Get the current node
        current_node = open_list[0]
        for node in open_list:
            if node.f < current_node.f:
                current_node = node

        open_list.remove(current_node)
        closed_list.append(current_node)

        # If we reached the end, return the path
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Check if the position is valid
            if (node_position[0] > (len(grid) - 1)) or (node_position[0] < 0) or (node_position[1] > (len(grid[len(grid)-1]) - 1)) or (node_position[1] < 0)):
                continue
            if grid[node_position[0]][node_position[1]] != 0:  # 0 means walkable
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if add_to_open(open_list, child):
                open_list.append(child)

    return None  # Return None if there is no path


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True

# Example usage:
if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]] # 0 is walkable, 1 is blocked
    start = (0, 0)
    end = (4, 4)
    path = astar(start, end, grid)
    print(path)  # Output the path