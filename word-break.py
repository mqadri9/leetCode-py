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
            
