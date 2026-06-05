class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        dict1={}
        dict2={}
        for i in range(len(t)):
            dict1[t[i]]=dict1.get(t[i],0)+1
        have=0
        need=len(t)
        res=[-1,-1]
        reslen=float("inf")
        l=0
        for r in range(len(s)):
            dict2[s[r]]=dict2.get(s[r],0)+1
            if s[r] in dict1 and dict1[s[r]]>=dict2[s[r]]:
                have+=1
            while have==need:
                if(r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                dict2[s[l]]-=1
                if s[l] in dict1 and dict2[s[l]]<dict1[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!= float("inf") else ""