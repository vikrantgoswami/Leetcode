class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsCountMap = {}
        for num in nums:
            if num in numsCountMap.keys():
                return True
            else:
                numsCountMap[num] = 1
        return False