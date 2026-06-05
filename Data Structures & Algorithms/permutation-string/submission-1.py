class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        windlen=len(s1)
        dict1={}
        for x in s1:
            dict1[x]=dict1.get(x,0)+1
        
        l=0
        for l in range(len(s2)-windlen+1):
            dict2={}
            for r in range(windlen):
                dict2[s2[l+r]]=dict2.get(s2[l+r],0)+1
            if dict1==dict2:
                return True
        
        return False

            
