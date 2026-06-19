class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        raw =len(matrix)
        col=len(matrix[0])
        f=[[0]*raw for i in range (col)]
        for i in range(col):
            for j in range(raw):
                f[i][j]=matrix[j][i]
        return f
