grid = {}
for i in range(1000):
    grid[str(i)] = []
    for it in range(1000):
        grid.setdefault(str(it),[]).append(0)

print(grid)
    
        
