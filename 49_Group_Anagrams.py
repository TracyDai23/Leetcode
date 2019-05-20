# 99.91% 
# Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string.
# Then, we sort each string in O(K \log K)O(KlogK) time.
# Space Complexity: O(NK), the total information content stored in ans

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #find new character combo, add to key and value; else add the string to value
        d={}
        for string in strs:
            key = ''.join(sorted(string)) # convert list to string in python!!! Can not use list as dictionary key, but can use tuple as key.
            if key in d.keys():
                d[key].append(string)
            else:
                d[key] = [string]
        return list(d.values())
 
 #Use tuple as key:
 class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
