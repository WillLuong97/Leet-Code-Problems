def main(): 
    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }

    visited = [] #list to store all the nodes that have been visited by the algorithm
    queue = [] #initialize a queue

    #if the graph is not empty, then we would first add the root node into the two lists: 
    queue.append('A')
    visited.append('A')

    #as long as the queue has an element appended from the graph, 
    #we will loop through them and append them into the list
    while queue: 
        #remove the first element in the queue
        s = queue.pop(0)
        print(s, end = " ")
        for neighbor in graph[s]:
            #if the particular has not been visited 
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

main()




    
