from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            ans = []
            top, bottom = 0, len(matrix) - 1
            left, right = 0, len(matrix[0]) - 1

            while top <= bottom and left <= right:
                for j in range(left, right + 1):
                    ans.append(matrix[top][j])
                top += 1

                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1

                if top <= bottom:
                    for j in range(right, left - 1, -1):
                        ans.append(matrix[bottom][j])
                    bottom -= 1

                if left <= right:
                    for i in range(bottom, top - 1, -1):
                        ans.append(matrix[i][left])
                    left += 1

            return ans


slt = Solution()
print(slt.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
