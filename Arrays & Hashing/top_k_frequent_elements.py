class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        uniques = []
        for n in nums:
            if not n in myDict:
                myDict[n] = 1
                uniques.append(n)
            else:
                myDict[n] += 1
        uniques.sort(reverse=True, key=myDict.get)
        return uniques[0:k]