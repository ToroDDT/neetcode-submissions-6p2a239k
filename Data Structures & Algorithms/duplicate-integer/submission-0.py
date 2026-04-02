class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = False
        numbers_array = {}
        for number in nums:
            if numbers_array.get(number) is None:
                numbers_array[number] = number
            else:
                has_duplicate = True

        return has_duplicate