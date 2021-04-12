from collections import deque

class Graph:
    
    matrix = []
    def __init__(self, goalx, goaly):
        with open('input.txt') as file:
            self.matrix = [[int(digit) for digit in line.split()] for line in file]
        self.goalx = goalx
        self.goaly = goaly
        self.path = False
    
    def isValid(self, row, col, visited):
        
        if row == self.goalx and col == self.goaly: #GOAL State Found!
            print ("GOAL STATE FOUND!")
            self.path = True
            return False
        
        # Stop if goal state is found!
        if self.path == True:
            return False
        
        if row < 0 or col < 0 or row > 11 or col > 11:
            return False       
        
        if visited[row][col] == True:
            return False
        
        if self.matrix[row][col] == False:
            return False
        
        return True
        
    def DFS(self, x, y, visited):
                
        global count
        
        visited[x][y] = True
        
        print(x, end = ",")
        print(y, end = " ")
        
        if self.isValid(x-1, y, visited): #Up
            print("UP")
            self.DFS(x-1, y, visited)
        if self.isValid(x, y-1, visited): #Left
            print("LEFT")
            self.DFS(x, y-1, visited)
        if self.isValid(x, y+1, visited): #Right
            print("RIGHT")
            self.DFS(x, y+1, visited)
        if self.isValid(x+1, y, visited): #Down
            print("DOWN")
            self.DFS(x+1, y, visited)   
        count = count + 1 

    def BFS(self, x, y):
        
        queue = deque()
        visited = [[ False for i in range(12)] for i in range(12)]
        queue.append((x, y))
        steps = 0
        
        while queue:
            node = queue.popleft() 
                
            x = node[0]
            y = node[1]
            print(node)
            
            if (x == self.goalx and y == self.goaly):
                print ("GOAL STATE FOUND!")
                return steps
     
            if x < 0 or y < 0 or x >= 12 or y >= 12 or visited[x][y] or self.matrix[x][y] == False:
                continue
            
            visited[x][y] = True;
            
            queue.append((x-1, y)) #UP
            queue.append((x, y-1)) #LEFT
            queue.append((x, y+1)) #RIGHT
            queue.append((x+1, y)) #DOWN
            
            steps += 1
        return steps
        
if __name__ == "__main__":
    goalx = 10
    goaly = 0
    visited = [[ False for i in range(12)] for i in range(12)]

    # Create Graph
    maze = Graph(goalx, goaly)

    count = 0
    startx = 4
    starty = 11

    maze.DFS(startx, starty, visited)

    count = count + 1
    print("Algorithm: DFS, Steps Taken: " + str(count))
    
    print("----------------------------------------------")
    
    count = maze.BFS(startx, starty)
    count = count + 1
    print("Algorithm: BFS, Steps Taken: " + str(count))