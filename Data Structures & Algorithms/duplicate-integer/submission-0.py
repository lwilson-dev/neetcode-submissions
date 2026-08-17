class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeTable = []
        for num in nums:
            if (num in dupeTable):
                return True
            dupeTable.append(num)
        return False
            
            

