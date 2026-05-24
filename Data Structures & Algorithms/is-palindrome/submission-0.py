class Solution:
    def isPalindrome(self, s: str) -> bool:
        #keep only alphanumeric chars, lowercased
        letters = "".join(c.lower() for c in s if c.isalnum())

        #iterate only through half (should match up to second half in reverse)
        for i in range(len(letters)//2):
            #set up pointers
            l = i
            r = -(i+1)

            #main operation (key comparison)
            if letters[l] != letters[r]:
                return False

        return True