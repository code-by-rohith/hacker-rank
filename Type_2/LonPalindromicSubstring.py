class Solution:
    def longestPalindrome(self, s):
        def is_palindrome(substr):
            return substr == substr[::-1]

        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_palindrome(s[i:j]) and len(s[i:j]) > len(longest):
                    longest = s[i:j]
        return longest
if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    result = sol.longestPalindrome(s)
    print("Longest palindromic substring:", result)
