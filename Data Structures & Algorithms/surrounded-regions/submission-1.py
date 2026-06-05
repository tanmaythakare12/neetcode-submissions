class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # ROWS, COLS = len(board), len(board[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # def capture():
        #     q = deque()
        #     for r in range(ROWS):
        #         for c in range(COLS):
        #             if ((r == 0 or r == ROWS - 1 or
        #                 c == 0 or c == COLS - 1) and
        #                 board[r][c] == "O"
        #             ):
        #                 q.append((r, c))
        #     while q:
        #         r, c = q.popleft()
        #         board[r][c] = "T"
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
        #                 q.append((nr, nc))

        # capture()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        #         elif board[r][c] == "T":
        #             board[r][c] = "O"

        q=deque()
        for r in range(len(board)):
            if board[r][0]=="O":
                q.append((r,0))
            if board[r][len(board[0])-1]=="O":
                q.append((r,len(board[0])-1))

        for c in range(len(board[0])):
            if board[0][c]=="O":
                q.append((0,c))
            if board[len(board)-1][c]=="O":
                q.append((len(board)-1,c))
        direct=[(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            r,c=q.popleft()
            board[r][c]="T"
            for dr,dc in direct:
                nr=dr+r
                nc=dc+c
                if nr<0 or nr>=len(board) or nc<0 or nc>=len(board[0]) or board[nr][nc]!="O":
                    continue
                q.append((nr,nc))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"