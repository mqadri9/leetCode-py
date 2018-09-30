class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def traverse(start, s, wordDict):
            res = False
            for word in wordDict:
                if s[start:start+len(word)] == word:
                    start += len(word)
                    if start == len(s):
                        return True
                    else:
                        res = traverse(start, s, wordDict)
                        if res:
                            return True
                        else:
                            start -= len(word)
            
            return res
        return traverse(0, s, wordDict, d)
            
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def traverse(s, wordDict, d):
            if s in d:
                return d[s]
            for n in range(1, len(s)+1):
                try:
                    considered = s[:n]
                    not_considered = s[n:]
                except:
                    considered = s
                    not_considered = ""
                if considered in wordDict:
                    if not_considered == "":
                        return True
                    res = traverse(not_considered, wordDict, d)
                    if res:
                        d[s] = True
                        return True
            d[s] = False
            return False
            
        d = {}
        return traverse(s, wordDict, d)
