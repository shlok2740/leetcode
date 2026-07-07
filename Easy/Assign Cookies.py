class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        s_count = 0
        g_count = 0

        while s_count < len(s) and g_count < len(g):
            if s[s_count] >= g[g_count]:
                g_count += 1
            s_count += 1

        return g_count

