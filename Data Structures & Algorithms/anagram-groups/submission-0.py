
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        listOfSublistAnagrams = []
        for word in strs:
            listOfLetters = list(word)
            listOfLetters.sort()
            sortedWordList = listOfLetters
            sortedWord = "".join(sortedWordList)
            if anagramDict.get(sortedWord) is None:
                anagramDict[sortedWord] = [word]
            else:
                listOfAnagrams = anagramDict.get(sortedWord)
                listOfAnagrams.append(word)
                anagramDict[sortedWord] = listOfAnagrams

        for value in anagramDict.values():
            listOfSublistAnagrams.append(value)

        return listOfSublistAnagrams

