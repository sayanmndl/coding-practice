class Solution:
    def cleanRoot(self, robot):
        visited = set()

        dirs = (-1,0,1,0,-1)

        def backtrack():
            # Turn around
            robot.turnRight()
            robot.turnRight()

            # move back to previous cell
            robot.move()

            # restore original direction
            robot.turnRight()
            robot.turnRight()

        def dfs(r,c,direction):
            visited.add((r,c))
            robot.clean()

            for i in range(4):
                new_dir = (direction) % 4
                nr = r + dirs[new_dir]
                nc = c + dirs[new_dir+1]

                if (nr, nc) not in visited and robot.move():
                    dfs(nr,nc,new_dir)

                    backtrack()
                
                #next direction
                robot.turnRight()

        dfs(0,0,0)
