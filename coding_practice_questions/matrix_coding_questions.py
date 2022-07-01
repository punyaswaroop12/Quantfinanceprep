# Spiral matrix
#########################################################
# https://leetcode.com/problems/spiral-matrix/

# Video link: https://www.youtube.com/watch?v=1ZGJzvkcLsA&t=94s
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        dir = 0
        left = 0
        right = cols - 1
        top = 0
        down = rows - 1
        res = []
        while top <= down and left <= right:
            if dir == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif dir == 1:
                for i in range(top, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif dir == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            elif dir == 3:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            dir = (dir + 1) % 4
        return res

