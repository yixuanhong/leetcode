class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        slow = 0 
        i = 0
        while i<n:
            while i<n and chars[i] =="":
                i +=1
            while i < n and chars[i] != "":
                chars[slow] = chars[i]
                slow +=1
                i +=1
            while i < n and char[i] == "":
                i +=1
            if i < n :
                chars[slow] = ""
                slow += 1
        chars = chars[:slow]

        def reverse(a,l,r):
            while l < r :
                a[l],a[r] = a[r],a[l]
                l += 1
                r -= 1

        reverse(chars, 0 ,len(chars)-1)

        start = 0 
        for j in range(len(chars)+1):
            if j == len(chars) or chars[j] =="":
                reverse(chars,start, j -1)
                start = j + 1
        return "".join(chars)