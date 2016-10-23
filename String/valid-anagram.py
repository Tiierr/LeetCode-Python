# Time:  O(n)
# Space: O(1)
#
# Given two strings s and t, write a function to
# determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1

        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1
            if count[c.lower()] < 0:
                return False

        return True

# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    print Solution().isAnagram("anagram", "nagaram")
    print Solution().isAnagram("cat", "rat")