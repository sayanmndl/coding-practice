from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        DRAW = 0
        MOUSE_WIN=1
        CAT_WIN=2
        MOUSE_TURN=0
        CAT_TURN=1

        # result[m][c][turn]
        # 0 = draw/unknown
        # 1 = mouse wins
        # 2 = cat wins
        result = [
            [
                [DRAW, DRAW]
                for _ in range(n)
            ] for _ in range(n)
        ]

        # dregree[m][c][turn]
        # number of legal moves from this state
        degree = [
            [
                [0,0]
                for _ in range(n)
            ]
            for _ in range(n)
        ]

        for mouse in range(n):
            for cat in range(n):
                # mouse can move to any neighbor
                degree[mouse][cat][MOUSE_TURN] = len(graph[mouse])

                # can can move to any but 0
                degree[mouse][cat][CAT_TURN] = sum(next_cat != 0 
                for next_cat in graph[cat])

        q = deque()

        # base case 1: mouse reches 0-> mouse wins
        for cat in range(1,n):
            for turn in [MOUSE_TURN, CAT_TURN]:
                result[0][cat][turn] = MOUSE_WIN
                q.append((0, cat, turn, MOUSE_WIN))

        # base case 2: mouse and cat at same node -> cat wind
        for node in range(1,n):
            for turn in [MOUSE_TURN, CAT_TURN]:
                result[node][node][turn] = CAT_WIN
                q.append((node, node, turn, CAT_WIN))

        # reutn all states that could move into (mouse, cat, turn)
        def get_parents(mouse, cat ,turn):
            parents = []
            # if its mouse's turn
            if turn == MOUSE_TURN:
                for prev_cat in graph[cat]:
                    if prev_cat == 0:
                        continue

                    parents.append((mouse, prev_cat, CAT_TURN))
            
            # if its cat's turn
            else:
                for prev_mouse in graph[mouse]:
                    parents.append((prev_mouse, cat, MOUSE_TURN))

            return parents

        # BFS
        while q:
            mouse, cat, turn, winner = q.popleft()
            for pm, pc, pturn in get_parents(mouse, cat, turn):
                # alreadt solved
                if result[pm][pc][pturn] != DRAW:
                    continue
                player = (
                    MOUSE_WIN if pturn==MOUSE_TURN else CAT_WIN
                )

                # case 1:
                if winner == player:
                    result[pm][pc][pturn] = player
                    q.append((pm,pc,pturn,player))

                # case 2:
                else:
                    degree[pm][pc][pturn] -= 1
                    if degree[pm][pc][pturn] == 0:
                        opponent = (
                            CAT_WIN if pturn == MOUSE_TURN else MOUSE_WIN
                        )
                        result[pm][pc][pturn] = opponent
                        q.append((pm,pc,pturn,opponent))

        # starting state
        return result[1][2][MOUSE_TURN]
