class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len (s2)):
            return False
        left, right = 0, len(s1)
        while right < len(s2):
            if (Counter(s1) == Counter(s2[left:right])):
                return True
            else:
                left+=1
                right +=1
        return Counter(s1) == Counter(s2[left:right])