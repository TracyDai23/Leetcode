class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #standardize p: 1)"X*.*X*" ; 2) "a*a"; 3)".."; 
        # p=list(p)
        # for i in range(len(p)):
        #     if p[i:i+2]== '.*':
        #         print('i:',i)
        #         n=2
        #         while i+n+1 <len(p) and p[i+n+1] == "*":
        #             p=p[:i+2]+p[i+n+2:]
        #             n+=2
        #         n=2
        #         while i-n>=0 and p[i-n+1] == "*":
        #             p=p[i:]
        #             n+=2
        #     # print('p: ',p)
        #     elif len(p)>0 and p[i] =='*':
        #         n=1
        #         # while i+n <len(p)-1 and p[i-1] == p[i+n]:
        #         #     p=p[:i+n]+p[i+n+1:]
        #         #     # print(p[:i+n]+p[i+n+1])
        #         #     n+=1
        #         # if p[i-1] ==p[i+n]:
        #         #     p=p[:i+n]
        #     # elif p[i:i+1] == '..':
        #     #     n=1
        #     #     while i+n <len(p) and p[i]==p[i+n]:
        #     #         p=p[:i+1]+p[i+2:]
        #     #         n+=1
        # print(p)
        
        p=p[::-1] #reverse p
        s=s[::-1] #reverse s
        
        print(p, s)
        
        while len(s) >0:
            i=0 #index for p
            j=0 #index for s
            if p[i] != '.' and p[i]!= '*':
                if p[i]!=s[j]:
                    return False
                else:
                    p=p[1:]
                    s=s[1:]
            elif p[i] == '.':
                p=p[1:]
                s=s[1:]
            elif i>= len(p)-1 and p[i] =='*': #need to return False when * has no "." or character ahead. 
                return False
            elif p[i] =='*':
                adv=p[i+1]
                if adv == '.' and i+2<len(p):
                    
                elif adv =='*': #for p has "**" pattern, return False
                    return False
                else:
                    while len(s)>0 and s[j]==adv:
                        s=s[1:]
                    if s!=p:
                        return False
                    
        return True  
