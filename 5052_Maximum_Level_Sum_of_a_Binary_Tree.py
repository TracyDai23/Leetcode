#first trial in contest
self.nmax = 0
        self.level = 0
        
        def dfs(root, nsum,k):
            if not root:
                return
            print(root.val, nsum, k, self.nmax, self.level)
            #base case:
            if k> self.level:
                print('hit base case')
                if self.nmax < nsum:
                    self.level = k
                    self.nmax = nsum
                nsum = 0
            #recursion:
            nsum +=root.val
            k=k+1
            dfs(root.left, nsum,k)
            dfs(root.right, nsum,k)
        dfs(root,0,1)
        return self.level-1
