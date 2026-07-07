class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old,rows,cols=image[sr][sc],len(image),len(image[0])
        
        if old!=newColor:
            q=collections.deque([(sr,sc)])
            
            while q:
                i,j=q.popleft()
                image[i][j]=newColor
                for (x,y) in ((i,j+1),(i,j-1),(i-1,j),(i+1,j)):
                    if 0<=x<rows and 0<=y<cols and image[x][y]==old:
                        q.append((x,y))
                        
        return image
