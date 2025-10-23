class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            kq=''
            for i in range(len(s)-1):
                char = (int(s[i])+int(s[i+1]))%10
                kq=kq+str(char)
            s=kq
        return s == s[::-1]

        

            
            