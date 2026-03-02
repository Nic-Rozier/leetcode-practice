class Solution:
    '''
    Brute force, checks list twice.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            for second in range(first+1,(len(nums))):
                if nums[first] + nums[second] == target:
                    return [first,second]

class Hash:
    '''
    Single passes hash map, stores target and checks dict for value.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        equals = {} #dict of complement, index

        for i in range(len(nums)):
            if nums[i] in equals:
                return [equals[nums[i]],i]
            equals[target - nums[i]] = i