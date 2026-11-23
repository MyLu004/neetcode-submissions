class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


    def addWord(self, word):
        cur = self #place the child at the root
        for c in word:
            if c not in cur.children:
                #if the children not in the list, insert it
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROWS,COLS = len(board), len(board[0]) #non-empty list board
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 
                or r == ROWS 
                or c == COLS 
                or (r,c) in visit 
                or board[r][c] not in node.children): 
                return 

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord: #if true | add to the result
                res.add(word)
            
            #recursive in 4 direction
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)


            visit.remove((r,c))
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
        return list(res)







