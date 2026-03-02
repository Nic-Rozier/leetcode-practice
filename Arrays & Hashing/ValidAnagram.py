class Solution:
    '''
    Checks to see if given string is an anagram.
    Works by sorting letters and checking equivalency.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)