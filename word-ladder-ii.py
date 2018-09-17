
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
        level, Graph = self.BFS(beginWord, endWord, wordList)
        optimal = level.get(endWord)
        if not optimal:
            return []
        res = []
        self.DFS(Graph, beginWord, endWord, level, optimal, [], res)
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
        Graph = {}
        level = {beginWord: 0}
        i = 1 
        frontier = [beginWord]
        found = False
        while frontier:
            next1 = []
            for u in frontier:
                Graph[u] = self.find_neighbours(u, wordList)
                for v in Graph[u]:
                    if endWord == v:
                        found = True
                    if v not in level:
                        level[v] = i
                        next1.append(v)
            if found:
                break
            frontier = next1
            i +=1
        return level, Graph
        
    def DFS(self, Graph, start, end, level, optimal, solution=[], res=[]):
        solution.append(start)
        if end==start and len(solution) ==  optimal + 1:
            res.append([c for c in solution])
        else:
            if len(solution) !=  optimal + 1:
                for next in Graph[start]:
                    if level[next]==level[start]+1:
                        self.DFS(Graph, next, end, level, optimal, solution, res)
        del solution[len(solution)-1]
        
