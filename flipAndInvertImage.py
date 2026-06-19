class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len (image)
        for _ in range (n):
            image[_][:]=image[_][::-1]
        for _ in range (n):
            for j in range(n):
                if image[_][j]==1:
                    image[_][j]=0
                else:
                    image[_][j]=1
        return image
