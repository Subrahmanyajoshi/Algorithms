from typing import List


class BFS:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(len(grid[i])):

                if grid[i][j] == '1':

                    grid[i][j] = '0'
                    count += 1
                    queue = [(i, j)]

                    while queue:

                        node = queue.pop(0)
                        i, j = node[0], node[1]

                        if i + 1 < rows and grid[i + 1][j] == '1':
                            grid[i + 1][j] = '0'
                            queue.append((i + 1, j))

                        if j + 1 < cols and grid[i][j + 1] == '1':
                            grid[i][j + 1] = '0'
                            queue.append((i, j + 1))

                        if i - 1 >= 0 and grid[i - 1][j] == '1':
                            grid[i - 1][j] = '0'
                            queue.append((i - 1, j))

                        if j - 1 >= 0 and grid[i][j - 1] == '1':
                            grid[i][j - 1] = '0'
                            queue.append((i, j - 1))

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]

    # Find total number of islands
    solution = BFS()
    print(solution.numIslands(grid=grid))
