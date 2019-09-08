# Trail in Contest

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)[::-1]
        print(arr2)
        arr1.append(1000000001)
        res = 0
        for i in range(1,len(arr1)-1):
            if arr1[i]<=arr1[i-1] or arr1[i]>= arr1[i+1]:
                if not arr2:
                    return -1
                while arr2:
                    candi= arr2.pop()
                    if candi>arr1[i-1]:
                        res+=1
                        arr1[i]=candi
                        # print('if: ',i,candi,arr2,arr1)
                        break
                    else:        
                        # print('else continue: ',i,candi,arr2,arr1)
                        continue

            print(arr1[i],arr1)
        return res
            
                    
