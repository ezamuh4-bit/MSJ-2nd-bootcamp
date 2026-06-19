class Solution:
    def reverseWords(self, s: str) -> str:
        my_string = s.split()
        v=""
        for i in my_string:
        
            v+=i[::-1]
            v+=" "
        return v[:-1]
