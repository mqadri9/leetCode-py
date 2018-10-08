class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def ispalendrome(s):
            h = len(s)-1 
            l = 0
            while(l<=h):
                if s[h] != s[l]:
                    return False
                l+=1
                h-=1
            return True
                
        def traverse(s, d):
            if s in d:
                return d[s]
            if len(s) == 1:
                d[s] = 0
                return 0
            minpartition = float("inf")
            for i in range(1, len(s)+1):
                sub1 = s[:i]
                if ispalendrome(sub1):
                    sub2 = s[i:]
                    if sub2:
                        ret = traverse(sub2, d) + 1
                        if ret < minpartition:
                            minpartition = ret
                    else:
                        minpartition = 0
            d[s] = minpartition
            return minpartition
        d = {}
        return traverse(s, d)
