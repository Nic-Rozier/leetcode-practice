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


class Hash:
    def isGram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True