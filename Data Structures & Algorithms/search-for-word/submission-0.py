class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if ((r < 0 or c < 0) or
                (r >= rows or c >= cols) or
                (r,c) in path or
                board[r][c] != word[i]):
                #out of bounds or we have already visited this spot on the board or the current character we are on is not in this spot in the word
                return False

            path.add((r,c))

            up = dfs(r+1,c,i+1)
            down = dfs(r-1,c,i+1)
            right = dfs(r,c+1,i+1)
            left = dfs(r,c-1,i+1)

            path.remove((r,c))
            if up or down or right or left:
                return True
            else:
                return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False


