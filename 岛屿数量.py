class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs( i, j, so):
            if i < 0 or j < 0 or i >= len(so) or j >= len(so[0]) or so[i][j] != '1':
                return
            so[i][j] = '0'
            dfs(i + 1, j, so)
            dfs( i - 1, j, so)
            dfs(i, j + 1, so)
            dfs(i, j - 1, so)
        if len(grid) == 0:
            return 0
        num = 0
        height = len(grid)
        width = len(grid[0])
        for h in range(height):
            for w in range(width):
                if grid[h][w] == '1':
                    dfs(h, w, grid)
                    num += 1
        return num 
