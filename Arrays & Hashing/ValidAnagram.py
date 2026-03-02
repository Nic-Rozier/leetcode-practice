class Solution:
    '''
    Checks to see if given string is an anagram.
    Works by sorting letters and checking equivalency.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    '''
    More efficient space wise than a hash map, but
    has to run the sorting algorithm.
    '''