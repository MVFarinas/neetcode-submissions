class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strlst1 = list(s)
        strlst2 = list (t)
        
        if len(strlst1) == len(strlst2):
            for char in strlst1:
                if char in strlst2:
                    strlst2.remove(char)
                else:
                    return False

        else:
            return False

        if len(strlst2) != 0:
            return False

        else:
            return True 