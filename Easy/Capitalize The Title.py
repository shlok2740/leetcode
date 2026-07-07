class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for s in title.split():
            if len(s) < 3:
                ans.append(s.lower())
            else:
                ans.append(s.capitalize())
        return ' '.join(ans)