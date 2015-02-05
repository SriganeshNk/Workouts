    def generateMatrix(n):
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        i = 1
        matrix =[[0 for x in range(n)] for y in range(n)]
        print matrix
        x, y, count = 0, 0, 1
        start_x, start_y, end_y = 0, 0, 0
        end_x = len(matrix)
        end_y = len(matrix[0])
        total = end_x * end_y 
        while x < len(matrix) and y < len(matrix[0]):
            while y < end_y and count <= total+1:
                matrix[x][y] = count
                count += 1
                y = y+1
            if count == total+1:
                break
            x = x+1
            y = y-1
            while x < end_x:
                matrix[x][y] = count
                x = x+1
                count += 1
            if count == total+1:
                break
            y = y-1
            x = x-1
            while y >= start_y:
                matrix[x][y] = count
                y = y-1
                count += 1
            if count == total+1:
                break
            y = y+1
            x = x-1
            while x > start_x:
                matrix[x][y] = count
                x = x-1
                count += 1
            if count == total+1:
                break
            start_x, start_y =  start_x + 1, start_y + 1
            end_x, end_y = end_x - 1, end_y - 1
            x, y = start_x, start_y
        i = 0
        print matrix
        return matrix


    generateMatrix(3)
