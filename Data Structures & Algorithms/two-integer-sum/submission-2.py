class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_num_dict = {} # {value, required_num}
        for i in range(0, len(nums)):
            required_num = target - nums[i]
            if required_num in required_num_dict:
                return [required_num_dict[required_num], i]
            required_num_dict[nums[i]] = i