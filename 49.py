class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {} # unique anagram : unique value
        result = [] # empty array
        for s in strs: 
            anagram = "".join(sorted(s)) # converts string to alphabetized version to use as anagram
            if not anagram in myMap: # if the anagram is new, add it to the map
                myMap[anagram] = len(result) # unique anagram : unique value (value depends on size of result array)
                result.append([])
            result[myMap[anagram]].append(s) # add the word to the corresponding array by using the map
        return result
