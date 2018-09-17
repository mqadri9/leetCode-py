

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord in wordList:
            return []
        self.Graph = {}
        self.BFS(beginWord, endWord, wordList)
        self.optimal = self.level.get(endWord)
        if not self.optimal:
            return []
        res = []
        self.DFS(beginWord, endWord, [], res)
        return res

    def differ_by_one(self, word1, word2):
        count_diffs = 0
        for a, b in zip(word1, word2):
            if a!=b:
                if count_diffs: return False
                count_diffs += 1
        return True

    def find_neighbours(self, u, wordList):
        neighbours = []
        for s in wordList:
            if u!=s and self.differ_by_one(u, s):
                neighbours.append(s)
        return neighbours  
    
    def BFS(self, beginWord, endWord, wordList):
        level = {beginWord: 0}
        i = 1 
        frontier = [beginWord]
        found = False
        while frontier:
            next1 = []
            for u in frontier:
                self.Graph[u] = self.find_neighbours(u, wordList)
                for v in self.Graph[u]:
                    if endWord == v:
                        found = True
                    if v not in level:
                        level[v] = i
                        next1.append(v)
            if found:
                break
            frontier = next1
            i +=1
        self.level = level
        
    def DFS(self, start, end, solution=[], res=[]):
        solution.append(start)
        if end==start and len(solution) ==  self.optimal + 1:
            res.append([c for c in solution])
        else:
            if len(solution) !=  self.optimal + 1:
                for next in self.Graph[start]:
                    if self.level[next]==self.level[start]+1:
                        self.DFS(next, end, solution, res)
        del solution[len(solution)-1]
        
            
        
        
                    
