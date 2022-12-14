import math

def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append([int(i) for i in list(line.strip())])
    
    # How many trees are visible from outside the grid?
    print("Part 1:", count_visible(grid))

    # What is the highest scenic score possible for any tree?
    print("Part 2:", count_scenic_score(grid))

# A tree's scenic score is found by multiplying together 
# its viewing distance in each of the four directions.
def count_scenic_score(grid):
    size = len(grid)
    max_score = 1

    for x in range(1, size-1):
        for y in range(1, size-1):
            tree = grid[x][y]

            top = [grid[i][y] for i in range(x)]
            bottom = [grid[i][y] for i in range(x+1, size)]
            left = [grid[x][i] for i in range(y)]
            right = [grid[x][i] for i in range(y+1, size)]

            # reverse to get same distance to tree
            top.reverse()
            left.reverse()
            
            max_score = max(max_score, scenic_score(tree, left, right, top, bottom))

    return max_score

def scenic_score(tree, left, right, top, bottom):
    directions = [left, right, top, bottom]
    direction_scores = []

    for direction in directions:
        direction_scores.append(visible_trees(tree, direction))

    return math.prod(direction_scores)

def visible_trees(tree, direction):
    seen_trees = 0
    for seen_tree in direction:
        seen_trees += 1
        if seen_tree >= tree:
            return seen_trees
    return seen_trees

# def visible: 
#   - a tree that is on one of the outer rows
#   - a tree that is visible from at least one side: 
#       that is (strictly) higher than all trees on at least 
#       one side of it (inc. top and bottom)
def count_visible(grid):
    size = len(grid)
    sum = 2*size + (size-2)*2

    for x in range(1, size-1):
        for y in range(1, size-1):
            tree = grid[x][y]

            top = [grid[i][y] for i in range(x)]
            bottom = [grid[i][y] for i in range(x+1, size)]
            left = [grid[x][i] for i in range(y)]
            right = [grid[x][i] for i in range(y+1, size)]

            sum += is_visible(tree, left, right, top, bottom)

    return sum

def is_visible(tree, left, right, top, bottom):
    if max(left) < tree:
        return 1
    elif max(right) < tree:
        return 1
    elif max(top) < tree:
        return 1
    elif max(bottom) < tree:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()