# --------------------------------------------------------------------------------------------------------
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
# Accepted
# --------------------------------------------------------------------------------------------------------


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = 0
        n = len(haystack)
        k = len(needle)
        if k == 0: return 0
        if n== 0: return -1
        if n<k : return -1
        while idx <= n - k:
            if haystack[idx] == needle[0]:
                if haystack[idx:idx+k] == needle:
                    return idx
            idx = idx + 1
        return -1
