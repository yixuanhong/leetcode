class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m = len(s), len(p)
        if m>n:
            return []
        
        def idx(ch:str) -> int:
            return ord(ch) - ord("a")
        
        need = [0] * 26
        win = [0] * 26
        for ch in p :
            need[inx(ch)] +=1
        
        res = []
        for i in range(m):
            win[idx(s[i])]+=1
        
        if win == need:
            res.append(0)

        for right in range(m,n):
            left = right - m
            win[idx(s[left])]-=1
            win[idx(s[right])] +=1
            if win == need:
                res.append(left + 1)

        return res