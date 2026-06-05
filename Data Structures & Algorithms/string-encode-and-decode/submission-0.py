class Solution:

    def encode(self, strs: List[str]) -> str:
        ens=""
        for s in strs:
            ens+=str(len(s))+'/:'+ s
        return ens
    def decode(self, s: str) -> List[str]:
        des=[]
        i=0
        while i<len(s):
            delim=s.find('/:',i)
            length=int(s[i:delim])
            str1=s[delim+2:delim+2+length]
            des.append(str1)
            i=delim+2+length
        return des
       