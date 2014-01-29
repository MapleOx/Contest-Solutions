def move(cur_pos, grid, visited):
    '''
    Input: cur_pos, a tuple of coordinates (r,c) representing the current position,
    grid, a 2D list representing all the intersections, and a list of coordinates 'visited'
    corresponding to intersections that have already been visited.
    Output: The length of the path taken if cur_pos is the final position. Otherwise, call the function again
    for each of the possible next positions.
    '''
    global path_lengths
    num_rows, num_cols = len(grid), len(grid[0])
    r, c = cur_pos[0], cur_pos[1]
    if r == num_rows - 1 and c == num_cols - 1 and grid[r][c] != '*':
        path_lengths.append(len(visited))
    else:
        possible_next_moves = []
        if grid[r][c] == '+':
            if r+1 < num_rows:
                possible_next_moves.append((r+1, c))
            if r-1 > -1:
                possible_next_moves.append((r-1, c))
            if c+1 < num_cols:
                possible_next_moves.append((r, c+1))
            if c-1 > 0:
                possible_next_moves.append((r, c-1))
        elif grid[r][c] == '|':
            if r+1 < num_rows:
                possible_next_moves.append((r+1, c))
            if r-1 > -1:
                possible_next_moves.append((r-1, c))
        elif grid[r][c] == '-':
            if c+1 < num_cols:
                possible_next_moves.append((r, c+1))
            if c-1 > 0:
                possible_next_moves.append((r, c-1))
        next_moves = [pos for pos in possible_next_moves if pos not in visited]
        for pos in next_moves:
            new_visited = visited + [pos]
            move(pos, grid, new_visited)
            
output = []    
for i in range(int(input())):    
    # Read input into variables
    r = int(input())
    c = int(input())
    city_grid = []
    for i in range(r):
        city_grid.append(list(input()))
    
    path_lengths = []
    move((0,0), city_grid, [(0,0)])
    if len(path_lengths) > 0:
        output.append(min(path_lengths))
    else:
        output.append(-1)

for k in output:
    print(k)

