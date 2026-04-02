
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKDict = {}
        amoutOf = []
        final = []
        for number in nums:
            if topKDict.get(number) is not None:
                continue
            topKDict[number] = nums.count(number)
        for key, value in topKDict.items():
            amoutOf.append([value, key])

        amoutOf.sort()
        for x in range(k):
            print(x)
            final.append(amoutOf.pop()[1])

        return final