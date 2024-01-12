class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element_count ={}
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1
        
        for num, count in element_count.items():
            if count > 2:
                occurrences_to_remove = count - 2
                cur_index = 0
                while occurrences_to_remove > 0 and cur_index < len(nums):
                    if nums[cur_index] == num:
                        nums.pop(cur_index)
                        occurrences_to_remove -= 1
                    else:
                        cur_index += 1
        return len(nums)

