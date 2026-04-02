class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersDict = {}
        twosumanswer = []
        possible = 0

        for index in range(len(nums)):
            if numbersDict.get(nums[index]) is not None:
                numbersArray: List = numbersDict.get(nums[index])
                numbersArray.append(index)
                numbersDict[nums[index]] = numbersArray
            else: 
                numbersDict[nums[index]] = [index]

        for number in nums:
            possible = target - number
            if nums.count(possible) == 1 and possible == number:
                continue
            if numbersDict.get(possible):
                if number == possible:
                    twosumanswer = numbersDict.get(possible)
                else:
                    higher = max(nums.index(possible), nums.index(number))
                    lower = min(nums.index(possible), nums.index(number))
                    twosumanswer.append(lower)
                    twosumanswer.append(higher)
                break
                
        return twosumanswer

 
             



 
             

