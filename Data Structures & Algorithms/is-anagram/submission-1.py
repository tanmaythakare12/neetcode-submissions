class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # count1={}
        # count2={}
        # for i in range(len(s)):
        #     count1[s[i]]=count1.get(s[i],0)+1
        #     count2[t[i]]=count2.get(t[i],0)+1
        # if count1==count2:
        #     return True
        # return False
        if len(s)!=len(t):
            return False
        count={}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
        
        for i in range(len(s)): 
            count[t[i]]=count.get(t[i],0)-1

            if count[t[i]]==0:
                del count[t[i]]
            elif count[t[i]]<0:
                return False
        return len(count)==0


