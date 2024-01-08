class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = []
        k = 0 
        for number in nums:
            if number not in num:
                num.append(number)
                k+=1
        nums[:] = num
        return k    
