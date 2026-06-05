class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dict1={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        res=[]
        def backtrack(idx,subset):
            if idx==len(digits):
                res.append("".join(subset))
                return
            d=digits[idx]
            for c in dict1[d]:
                subset.append(c)
                backtrack(idx+1,subset)
                subset.pop()
        backtrack(0,[])
        return res