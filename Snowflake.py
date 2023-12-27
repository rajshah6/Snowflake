while True:
    # get correct input
    while True:
        try:
            n = int(input("Enter an odd integer: "))
            if n % 2 == 0 or n <= 0:
                continue
            else:
                break

        except ValueError:
            continue

        else:
            break

    # make the grid
    def displayGrid():
        for i in grid:
            print(" ".join(i))

    grid = [["."] * n for i in range(n)]

    # iterate through grid
    for rowIdx, rowVal in enumerate(grid):
        for elemIdx, elemVal in enumerate(rowVal):
            # vertical line
            if elemIdx == n // 2:
                grid[rowIdx][elemIdx] = "*"
            
            # horizontal line
            if rowIdx == n // 2:
                grid[rowIdx][elemIdx] = "*"

    # diagonals:
    diagonal1 = 0
    diagonal2 = n-1

    for rowIdx, rowVal in enumerate(grid):
        for elemIdx, elemVal in enumerate(rowVal):
            if elemIdx == diagonal1:
                grid[rowIdx][elemIdx] = "*"
                break
        
        diagonal1 += 1

    for rowIdx, rowVal in enumerate(grid):
        for elemIdx, elemVal in enumerate(rowVal):
            if elemIdx == diagonal2:
                grid[rowIdx][elemIdx] = "*"
                break
        
        diagonal2 -= 1

    displayGrid()