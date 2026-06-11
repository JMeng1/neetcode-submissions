class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_num_dict = {} # {value, required_num}
        for value, num in enumerate(nums):
            required_num = target - num
            if required_num in required_num_dict:
                return [required_num_dict[required_num], value]
            required_num_dict[num] = value