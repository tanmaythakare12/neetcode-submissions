class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        windlen=len(s1)
        dict1={}
        dict2={}
        for x in range(len(s1)):
            dict1[s1[x]]=dict1.get(s1[x],0)+1
            dict2[s2[x]]=dict2.get(s2[x],0)+1
        
        if dict1==dict2:
            return True
        
        for i in range(len(s1),len(s2)):
            dict2[s2[i]]=dict2.get(s2[i],0)+1
            dict2[s2[i-len(s1)]]-=1
            if dict2[s2[i-len(s1)]]==0:
                del dict2[s2[i-len(s1)]]
        
            if dict1==dict2:
                return True
        
        return False

            
