class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []

        for key in s:
            sList.append(key)
        for key in t:
            tList.append(key)
        for key in sList:
            if key not in tList:
                return False
            if key in tList:
                tList.remove(key)
        if len(tList) == 0:
            return True
        return False