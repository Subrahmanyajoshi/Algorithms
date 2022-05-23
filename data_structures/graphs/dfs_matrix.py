from typing import List


class DFS:

    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.cols = len(grid[0])
        self.rows = len(grid)

    def dfs(self, r, c):

        if r < 0 or c < 0 or r >= self.rows or c >= self.cols or self.grid[r][c] == '0':
            return

        self.grid[r][c] = '0'
        self.dfs(r - 1, c)
        self.dfs(r, c - 1)
        self.dfs(r + 1, c)
        self.dfs(r, c + 1)

    def numIslands(self) -> int:

        count = 0

        for i in range(self.rows):
            for j in range(self.cols):

                if grid[i][j] == '1':
                    count += 1

                    self.dfs(i, j)

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

    # Find total number of islands
    solution = DFS(grid=grid)
    print(solution.numIslands())
