class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def traverse(n, start, closed, opened):
            if closed == 0 and opened ==0:
                self.solutions.append(start)
                return
            flag = False
            if closed !=0 and opened < closed:
                flag = True
                closed-=1
                start = start+")"
                traverse(n, start, closed, opened)
            if opened != 0:
                opened-=1
                if flag:
                    start =  start[:-1]
                    closed+=1
                start += "("
                traverse(n, start, closed, opened)
                
        self.solutions = []
        traverse(n,"(", n, n-1)
        return self.solutions
