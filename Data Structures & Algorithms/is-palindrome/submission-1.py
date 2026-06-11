class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_ptr = 0
        second_ptr = len(s)-1
        while first_ptr <= second_ptr:
            while first_ptr <= second_ptr and s[first_ptr].isalnum() != True:
                first_ptr += 1
            while first_ptr <= second_ptr and s[second_ptr].isalnum() != True:
                second_ptr -= 1
            if first_ptr <= second_ptr:
                if s[first_ptr].lower() == s[second_ptr].lower():
                    first_ptr += 1
                    second_ptr -= 1
                else:
                    return False
        return True