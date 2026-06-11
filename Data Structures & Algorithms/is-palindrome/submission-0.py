class Solution:
    def isPalindrome(self, s: str) -> bool:
        create_new_str = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                create_new_str += (s[i])
        create_new_str = create_new_str.lower()
        first_ptr = 0
        second_ptr = len(create_new_str)-1
        while first_ptr <= second_ptr:
            if create_new_str[first_ptr] == create_new_str[second_ptr]:
                first_ptr += 1
                second_ptr -= 1
            else:
                return False
        return True