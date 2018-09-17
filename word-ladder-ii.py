class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.construct_graph(beginWord, wordList)
        self.BFS(beginWord)
        self.optimal = self.level[endWord]
        res = []
        self.DFS(beginWord, endWord, [], res)
        print res

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
        i = 1 
        frontier = [beginWord]
        while frontier:
            next1 = []
            for u in frontier:
                for v in self.Graph[u]:
                    if v not in level:
                        level[v] = i
                        next1.append(v)
            frontier = next1
            i +=1
        self.level = level
        
    def DFS(self, start, end, solution=[], res=[]):
        solution.append(start)
        if end==start:
            res.append([c for c in solution])
        else:
            for next in self.Graph[start]:
                if self.level[next]==self.level[start]+1:
                    self.DFS(next, end,  solution, res)
        del solution[len(solution)-1]
        
            
        
        
                    
