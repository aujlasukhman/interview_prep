from collections import defaultdict
def findItinerary(tickets):
        output = []
        '''more or less my way'''

#         myDict = {}
#         for ticket in tickets:
#             if ticket[0] in myDict:
#                 myDict[ticket[0]].append(ticket[1])
#                 myDict[ticket[0]].sort(reverse = True)
#             else:
#                 myDict[ticket[0]] = [ticket[1]] # could try and use deque here
#         #print(myDict)
#         #print(len(myDict['JFK']))
#         def helper(myDict,city):
#             if city in myDict:
#                 while len(myDict[city]) != 0:
#                     new_city = myDict[city].pop()
#                     #print(new_city)
#                     #print(type(new_city))
#                     helper(myDict,new_city)
#             nonlocal output
#             output.append(city)
                
        
#         helper(myDict,'JFK')

        '''well, not my way'''

        graph = defaultdict(list)
        '''print(sorted(tickets))'''
        ''' could try and sort them here and then call them from end and also discard sort in the for loop '''
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
            graph[ticket[0]].sort(reverse = True)
        #print(graph)

        def visit(airport):
            while len(graph[airport]) != 0:
                visit(graph[airport].pop())
            nonlocal output
            output.append(airport)
            return

        visit('JFK')      

        return output[::-1]



print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))