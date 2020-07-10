# #Python program to find the shortest path possible between two nodes in a graph using Breadth First Search algorithm
# import queue
# LIST_OF_POSSIBLE_MOVES = ['U', 'D', 'L', 'R']


# #Creating a 2d array from a list
# # def create_array_from_list(listOfElement):
# #     #width and height of the 2d array based on the list dimension
# #     w = len(listOfElement[0])
# #     h = len(listOfElement)
# #     #Creating a 2d array based on the elements in the list
# #     board = []
# #     for i in range(w):
# #         sub = []
# #         for j in range(h):
# #             sub.append(listOfElement[i][j])
# #         board.append(sub)
# #     for row in board:
# #         print(board)
    
# #     return board

# #Fucntion to find the shortest between the starting nodes and ending nodes
# def find_shortest_path(start, end, maze):
#     #create a queue to store the values
#     q = queue.Queue()
#     q.put("")
#     nodes = ""
#     #as long as the current nodes is not the ending position
#     while not isFinalNode(maze, nodes):
#         node = q.get()
#         #checking the moves of the current node
#         for i in LIST_OF_POSSIBLE_MOVES:
#             #moving the nodes by adding its possible moves to the queue.
#             node = node + i
#             #check to see if the moves are valid
#             if valid_path(maze, node, start):
#                 q.put(node)
   
    
# #Function to check if the current nodes is the destination node: 
# def valid_path(maze, path, start):
#     for x, pos in enumerate(maze[0]):
#         if pos == start:
#             #marked the path moving along: 
#             waypoints = x
#     i = waypoints
#     j = 0
#     #looping through the potential potentials:
#     for moves in path:
#         #Valid moves:
#         if moves == "L":
#             i -= 1

#         elif moves == "R":
#             i += 1
        
#         elif moves == "U":
#             j -= 1

#         elif moves == "D":
#             j += 1
        
#         #if the path goes out of the maps
#         if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
#             return False

#         #If the path runs into a wall
#         elif maze[j][i] == 1:
#             return False
        
#     return True

# #Function to check for the valid path between each nodes
# def isFinalNode(maze, path):
#     for x, pos in enumerate(maze[0]):
#         if pos == maze[0][0]:
#             #marked the path moving along: 
#             waypoints = x
#     i = waypoints
#     j = 0
#     #looping through the potential potentials:
#     for moves in path:
#         #Valid moves:
#         if moves == "L":
#             i -= 1

#         elif moves == "R":
#             i += 1
        
#         elif moves == "U":
#             j -= 1

#         elif moves == "D":
#             j += 1
        
#     #if the maze reaches the desintaion nodes in our game: 
#     if(maze[j][i] == end):
#         print("Found: " + path)
        
#         return True
    
#     return False
# #main function to run the program
# def main(): 
#     maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
#     #Extracting the dimension of the maze
#     w = len(maze[0])
#     h = len(maze)
#     #extracting the starting and ending nodes of the maze
#     starting_node = maze[0][0]
#     destination_node = maze[h-1][w-1]
#     #function to find the shortest path between two nodes
#     print(find_shortest_path(starting_node, destination_node, maze))
# main()


def shortest_path(sx, sy, maze):
    w = len(maze[0])
    h = len(maze)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]

    for rows in board:
        print(rows)
    print("")
    while arr:
        x, y = arr.pop(0)
        #the possible moves a node can move along the path
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
         #making the node move by adding the nodes to its
         # moves
          nx, ny = x + i[0], y + i[1]
          #make sure that the bunny is not moving away from
          # the map. (Out-of-bound checks)
          if 0 <= nx < h and 0 <= ny < w:
              
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if maze[nx][ny] == 1 :
                  continue
                arr.append((nx, ny)) 
    # for rows in board:
    #     print(rows)

    return board

def solution(maze):
    #getting the dimension of a maze
  w = len(maze[0]) #width
  h = len(maze) #height
  tb = shortest_path(0, 0, maze)
  bt = shortest_path(h-1, w-1, maze)

  ans = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          if tb[i][j] and bt[i][j]:
              ans = min(tb[i][j] + bt[i][j] - 1, ans)
  return ans

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(maze))