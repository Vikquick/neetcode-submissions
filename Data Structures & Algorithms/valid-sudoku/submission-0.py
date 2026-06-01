class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = True
        for line in board:
            line = [x for x in line if x != '.']
            if len(line) != len(set(line)):
                a=False
        for i in range(len(board)):
            s = []
            for line in board:
                if line[i] != '.':
                    s.append(line[i])
            if len(s) != len(set(s)):
                a=False
        squares = [[0, 3], [3, 6], [6, 9]]
        for rows in squares:
            for cols in squares:
                s = []

                for r in range(rows[0], rows[1]):
                    for c in range(cols[0], cols[1]):
                        if board[r][c] != '.':
                            s.append(board[r][c])

                if len(s) != len(set(s)):
                    a = False

        return a