class Solution:
    '''
    Sets can only contain unique elements. If the length of the list is the
    same as the set, it contains no duplicates.
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True