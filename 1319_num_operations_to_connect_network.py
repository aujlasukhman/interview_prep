from collections import defaultdict

def makeConnected(n: int, connections) -> int:
    if len(connections) < n-1:
        return -1
    '''
    make a graph and then do dfs from node1 and then identify clusters
    '''
    graph = defaultdict(list,[(i,[]) for i in range(n)])
    #graph = {i:[] for i in range(n)}
    #print(type(graph))
    #print(graph)
    
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])
    
    #print(graph)
    #print(connections[0][0])
    #print(graph[6])
    
    visited = set()
    
    def traversal(computer):
        if computer in visited:
            return
        visited.add(computer)
        for neighbor in graph[computer]:
            #print(neighbor)
            traversal(neighbor)
            

    cluster = 0
    for node in graph:
        if node not in visited:
            traversal(node)
            cluster += 1
    
    return cluster - 1


    '''
    union find, couldn't solve it to save my life
    '''
    
    '''
    connected_comps = [i for i in range(n)]
    unique_set = set()
    
    def findparent(computer):
        if connected_comps[computer] == computer:
            return computer
        else:
            parent = findparent(connected_comps[computer])
            #connected_comps[computer] = parent
            return parent
        
    def fixparent(computer):
        if connected_comps[computer] == computer:
            return computer
        else:
            parent = fixparent(connected_comps[computer])
            connected_comps[computer] = parent
            return parent
    
    '''
    '''
    0,1,2,3
    [3,1,3,3]
    '''
    '''
    for connection in connections:
        parent0 = findparent(connection[0])
        parent1 = findparent(connection[1])
        #print(parent0,parent1)
        if parent0 == connection[0] and parent1 != connection[1]:
            connected_comps[connection[0]] = parent1
            connected_comps[connection[1]] = parent1
        elif :
            connected_comps[connection[0]] = parent0
            connected_comps[connection[1]] = parent0
        print(connected_comps)
        
#             if connected_comps[connection[1]] == connection[1]: # if it's self connected
#                 connected_comps[connection[1]] = fixparent(connection[0])
#             else:
#                 connected_comps[connection[1]] == connected_comps[connection[0]]
            
    
    
    for comp in range(len(connected_comps)):
        if comp == connected_comps[comp]:
            unique_set.add(comp)
    #print(connected_comps)
    print(unique_set)
    return len(unique_set) - 1
    
    '''
        
    
'''
0,1,2,3,4,5,6,7,8,9
[0,6,1,3,6,6,6,7,6,0]
'''         

print(makeConnected(10,[[6,8],[0,4],[1,2],[5,8],[0,9],[1,8],[1,4],[4,9],[4,6],[3,7],[2,4],[3,5],[6,7],[4,5]]))
print(makeConnected(11,[[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]))
print(makeConnected(5,[[0,1],[0,2],[3,4],[2,3]]))