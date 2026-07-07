class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        score=[[0]*8 for _ in range(2)]
        
        for i,(a,b) in enumerate(moves):
            i%=2
            score[i][a]+=1
            score[i][3+b]+=1
            if a==b:
                score[i][6]+=1
            if a+b==2:
                score[i][7]+=1
            
            
            if any(x==3 for x in score[i]):
                return "AB"[i]
            
        return "Pending" if len(moves)<9 else "Draw"