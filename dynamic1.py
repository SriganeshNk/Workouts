class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        Cost =[]
        if len(grid) <= 0 or len(grid[0]) <=0:
            return 0
        for x in range(len(grid)):
            L = []
            for y in range(len(grid[0])):
                if x == 0:
                    if y == 0:
                        L.append(grid[x][y])
                    else:
                        L.append(grid[x][y]+L[y-1])
                if y == 0 and x != 0:
                    L.append(grid[x][y]+Cost[x-1][y])
                if x > 0 and  y > 0:
                    L.append(-1)
            Cost.append(L)
        x, y = 0, 0
        while x < len(grid):
            y = 0
            while y < len(grid[0]):
                if Cost[x][y] == -1:
                    print Cost[x][y], grid[x][y], "COST and Grid"
                    print Cost[x-1][y], Cost[x][y-1], "Only Cost"
                    Cost[x][y] = min(Cost[x-1][y], Cost[x][y-1]) + grid[x][y]
                y += 1
            x += 1
        print Cost
        return Cost[len(grid)-1][len(grid[0])-1]

s = Solution()
grid =[[1,2],[1,1]]
print len(grid), len(grid[0])
print s.minPathSum(grid)
