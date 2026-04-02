
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalProduct = []
        product = None
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums):
                if j == i:
                    j += 1
                    continue
                elif product is None:
                    product = nums[j]
                    j += 1
                else:
                    product *= nums[j]
                    j += 1
            i += 1
            j = 0
            finalProduct.append(product)
            product = None
        return finalProduct


