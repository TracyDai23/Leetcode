#Optimized solution: 
#add dash from back of the list. S[::-1], syntax to reverse string.

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #requirements: 1) upper case, 2) exact characters of k len(S)%k will be first section length; 3) how to count len(S) without dash
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1] # range(start, end, steps) 
    # the slicing syntax has supported an optional third ``step'' or ``stride'' argument. For example, these are all legal Python syntax: L[1:10:2], L[:-1:1], L[::-1]
    #https://docs.python.org/2.3/whatsnew/section-slices.html






#My own solution:

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #requirements: 1) upper case, 2) exact characters of k len(S)%k will be first section length; 3) how to count len(S) without dash
        st = ''
        st=S.replace('-','').upper()
        c=len(st)
        if not c :
            return st
        else:
        # for i in range(len(S)):
        #     if S[i] != '-':
        #         st = st+ S[i]
        #         c=c+1
        # st=st.upper()
        #c is total length of S without dash
            left= c%K
            O=st[:left]
            for i in range(c//K):
                O = O+'-'+ st[left+K*i:left+K*(i+1)]
            if  O[0] == '-':
                O=O[1:]
            return O
            
