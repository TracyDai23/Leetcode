// logic: https://www.youtube.com/watch?v=LPFhl65R7ww&feature=emb_logo
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (n < m):
            return self.findMedianSortedArrays(nums2, nums1)
        
        nums1 = [-math.inf] +nums1 +[math.inf]
        nums2 = [-math.inf] +nums2 +[math.inf]
        # print(nums1)
        isOdd = ((m+n)%2 != 0)
        l = m//2
        while (l>=0 and l<=m):
            r = (m+n+1)//2 -l                
            
            if (nums1[l] <= nums2[r+1]) and (nums2[r]<= nums1[l+1]): 
                if (isOdd):
                    return max(nums1[l], nums2[r])
                else: 
                    return (max(nums1[l], nums2[r])+ min(nums1[l+1], nums2[r+1]))/2
                
            elif nums1[l] > nums2[r+1]:
                l-=1
            else:
                l+=1
