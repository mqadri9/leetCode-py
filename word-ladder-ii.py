class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.construct_graph(beginWord, wordList)
        self.BFS(beginWord)
        s = endWord
        answer = []
        while s != beginWord:
            answer.append(s)
            s = self.parent[s]
        print answer
        
    def differ_by_one(self, word1, word2):
        if word1 == word2:
            return False
        diff_one = False
        for i in range(len(word1)):
            if word2[i] != word1[i]:
                if not diff_one:
                    diff_one = True
                else:
                    return False
        return True
    
    def construct_graph(self, beginWord, wordList):
        self.Graph = {}
        complete = wordList
        complete.extend([beginWord])
        for s in complete:
            self.Graph[s] = []
            for e in wordList:
                if self.differ_by_one(e, s):
                    self.Graph[s].append(e)
                    

    def BFS(self, beginWord):
        level = {beginWord: 0}
        parent = {beginWord: None}
        i = 1 
        frontier = [beginWord]
        while frontier:
            next1 = []
            for u in frontier:
                for v in self.Graph[u]:
                    if v not in level:
                        level[v] = i
                        parent[v] = u 
                        next1.append(v)
            frontier = next1
            i +=1
        self.parent = parent
        
