class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = []
        two = []
        for character in s:
            one.append(character)
        
        for character in t:
            two.append(character)
            
        one.sort()
        two.sort()
        
        finalOne = "".join(one)
        finalTwo = "".join(two)
        
        if finalOne == finalTwo:
            return True
        return False