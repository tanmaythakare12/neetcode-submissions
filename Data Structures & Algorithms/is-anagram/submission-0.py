class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1={}
        count2={}
        for i in range(len(s)):
            count1[s[i]]=count1.get(s[i],0)+1
            count2[t[i]]=count2.get(t[i],0)+1
        if count1==count2:
            return True
        return False
