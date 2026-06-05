class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,r):
            i=0
            j=0
            ans=[]
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    ans.append(l[i])
                    i+=1
                else:
                    ans.append(r[j])
                    j+=1
            while i<len(l):
                ans.append(l[i])
                i+=1
            while j<len(r):
                ans.append(r[j])
                j+=1
            return ans



        def mergesort(arr):
            if len(arr)<=1:
                return arr

            mid=len(arr)//2
            left=mergesort(arr[:mid])
            right=mergesort(arr[mid:])
            return merge(left,right)
        return mergesort(nums)
        