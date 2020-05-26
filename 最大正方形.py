class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        height = len(matrix)
        width = len(matrix[0])
        res = 0
        sol = list()
        #print(sol)
        for i in range(height+1):
            sol.append([0]*(width+1))
        for start_point_height in range(1, height+1):
            for start_point_width in range(1, width+1):
                end_point_height = start_point_height  -1
                end_point_width = start_point_width -1
                if (matrix[end_point_height][end_point_width] == '1'):
                    sol[start_point_height][start_point_width] = min(
                        sol[start_point_height][end_point_width], 
                        sol[end_point_height][start_point_width], 
                        sol[end_point_height][end_point_width]) + 1
                    res = max(res, sol[start_point_height][start_point_width])
        return res * res
