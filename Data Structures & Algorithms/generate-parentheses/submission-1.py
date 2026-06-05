class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack=[]
        # res=[]
        # def backtrack(openx,closex):
        #     if openx==closex==n:
        #         res.append("".join(stack))
        #         return
        #     if openx<n:
        #         stack.append("(")
        #         backtrack(openx+1,closex)
        #         stack.pop()
        #     if closex<openx:
        #         stack.append(")")
        #         backtrack(openx,closex+1)
        #         stack.pop()
        # backtrack(0,0)
        # return res

        stack=[]
        res=[]
        def backtrack(openx,closex):
            if openx==closex==n:
                res.append("".join(stack))
                return
            if openx<n:
                stack.append("(")
                backtrack(openx+1,closex)
                stack.pop()
            if closex<openx:
                stack.append(")")
                backtrack(openx,closex+1)
                stack.pop()
        backtrack(0,0)
        return res