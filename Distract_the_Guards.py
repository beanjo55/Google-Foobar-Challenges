# FOOBAR Level 4 - Distract the Guards
#
# The time for the mass escape has come, and you need to distract the guards so 
# that the bunny prisoners can make it out! Unfortunately for you, they're 
# watching the bunnies closely. Fortunately, this means they haven't realized yet 
# that the space station is about to explode due to the destruction of the 
# LAMBCHOP doomsday device. Also fortunately, all that time you spent working as 
# first a minion and then a henchman means that you know the guards are fond of 
# bananas. And gambling. And thumb wrestling.
#
# The guards, being bored, readily accept your suggestion to play the Banana 
# Games.
#
# You will set up simultaneous thumb wrestling matches. In each match, two guards 
# will pair off to thumb wrestle. The guard with fewer bananas will bet all their 
# bananas, and the other guard will match the bet. The winner will receive all of 
# the bet bananas. You don't pair off guards with the same number of bananas (you 
# will see why, shortly). You know enough guard psychology to know that the one 
# who has more bananas always gets over-confident and loses. Once a match begins, 
# the pair of guards will continue to thumb wrestle and exchange bananas, until 
# both of them have the same number of bananas. Once that happens, both of them 
# will lose interest and go back to guarding the prisoners, and you don't want 
# THAT to happen!
# 
# For example, if the two guards that were paired started with 3 and 5 bananas, 
# after the first round of thumb wrestling they will have 6 and 2 (the one with 3 
# bananas wins and gets 3 bananas from the loser). After the second round, they 
# will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they 
# stop and get back to guarding.
#
# How is all this useful to distract the guards? Notice that if the guards had 
# started with 1 and 4 bananas, then they keep thumb wrestling! 
# 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.
#
# Now your plan is clear. You must pair up the guards in such a way that the 
# maximum number of guards go into an infinite thumb wrestling loop!
# 
# Write a function answer(banana_list) which, given a list of positive integers 
# depicting the amount of bananas the each guard starts with, returns the fewest 
# possible number of guards that will be left to watch the prisoners. Element i of 
# the list will be the number of bananas that guard i (counting from 0) starts 
# with.
#
# The number of guards will be at least 1 and not more than 100, and the number of 
# bananas each guard starts with will be a positive integer no more than 
# 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

# This is a helper function to help us answer this problem, which consists of 
# two parts: 
#      1) Identifying which guards can play against each other and loop, 
#         essentially creating the edges of a graph. This part is done in the
#         calling function - answer().
#      2) Finding the maximum matching in the created graph so that we can find
#         the greatest number of guards who can play each other and end up in
#         an infinite loop. This part is done in this function - 
#         maximum_matching() - using the blossom algorithm.
def maximum_matching(graph):
    
    # First, we need a list of edges in the graph - those part of the matching
    # and those not part of the matching. Originally, none of the edges are part
    # of the matching.
    nonmatchingEdges = [[x, y] for x in range(len(graph)) 
                        for y in range(len(graph[x]))
                        if graph[x][y] == 1]
    matchingEdges = [] 
    
    # The current nodes not in our maximum matching - an easier structure to use
    # as starting nodes for DFS
    nonmatching = [x for x in range(len(graph))]

    # While we are still able to find an augmented path...
    pathFound = True
    while pathFound:
        
        # Set the tracker here. If an augmented path is found, pathFound will be
        # True
        pathFound = False
    
        # Check all paths starting at each node that is not part of the current
        # maximum matching
        for j in nonmatching:
            
            # Visited graph - which nodes have been visited?
            visited = []
            
            # The augmented path, implemented as a stack. The stack will add a 
            # node if the node is connected to at least one other unvisited 
            # node. The node on the top of the stack will be popped otherwise.
            path = []
            
            # Start the path at an entrance
            node = j                  
            
            # The blossom algorithm defines an augmented path as a path with 
            # edges alternating between those in the matching and those not in
            # the matching. Every time we add an edge to the path, we flip this
            # boolean value.
            edgeNotInMatching = True
            while 1:
                
                # Keep track of whether or not we have found an unvisited node
                # connected to our current node of interest
                findUnvisited = False   
                
                # Also keep track of visited nodes
                visited.append(node)      
                
                # Check all adjacent nodes for one that is unvisited and the edge
                # it makes with the current node matches whether or not we need
                # an edge in the current matching or an edge not in the current 
                # matching.
                index = 0                
                for i in range(len(graph[node])):
                    if i not in visited and graph[node][i] != 0:
                        if ((edgeNotInMatching and [node, i] in nonmatchingEdges) 
                            or (not edgeNotInMatching and [node, i] in matchingEdges)):
                            edgeNotInMatching = not edgeNotInMatching
                            index = i
                            findUnvisited = True
                            break   
                
                # Go to the found node
                if findUnvisited:
                    path.append(node)
                    node = index
                
                # If there are no unvisited nodes connected to this entrance, 
                # check the paths connecting to another entrance.
                elif not path:
                    break   
                
                # If there are no unvisited nodes connected, backtrace in the 
                # augmented path.
                else:
                    node = path.pop()
                    edgeNotInMatching = not edgeNotInMatching
                
                # If we find an end node, update the matching by putting edges
                # in the augmented path in the matching if they weren't in the
                # matching before or taking them out if they were in the 
                # matching before. Also add the first and last node in the path,
                # because the updated matching will now include them.
                if node in nonmatching and node != j:
                    path.append(node) 
                    pathFound = True           
                    for i in range(len(path) - 1):
                        if [path[i], path[i + 1]] in matchingEdges:
                            matchingEdges.remove([path[i], path[i + 1]])
                            matchingEdges.remove([path[i + 1], path[i]])
                            nonmatchingEdges.append([path[i], path[i + 1]])
                            nonmatchingEdges.append([path[i + 1], path[i]]) 
                        else:
                            nonmatchingEdges.remove([path[i], path[i + 1]])
                            nonmatchingEdges.remove([path[i + 1], path[i]])
                            matchingEdges.append([path[i], path[i + 1]])
                            matchingEdges.append([path[i + 1], path[i]])  
                    nonmatching.remove(path[0])
                    nonmatching.remove(path[len(path) - 1])
                    break
    
    # Return the number of nodes not part of the maximum matching. 
    return len(nonmatching)

# In order to create the edges of our graph, we need to determine which numbers
# in the given list can pair up and cycle. This requires a bit of mathematical
# proofing. First, it's important to note our representation of a graph in this
# problem - a square matrix in which the value at [i][j] == 0 if there is no
# edge between nodes i and j (in other words, guard i and guard j will not loop
# if they play each other) and == 1 if there is an edge between nodes i and j.
#
# To determine whether two numbers will actually loop, one needs to think a bit
# about the math, in particular what happens if both of the guards have even
# numbers of bananas or both of the guards have odd numbers of bananas.
def answer(banana_list):
    
    # First, make an array indicating which guards can play which guards and 
    # enter an infinite loop. 
    pairs = [[0 for y in banana_list] for x in banana_list]
    
    # For each guard, go through their possible partners and determine whether
    # they can play them and enter an infinite loop. 
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            
            guardi, guardj = banana_list[i], banana_list[j]
            
            # If the sum of the number of bananas the guards have is odd, 
            # clearly it's an infinite loop.
            if (guardi + guardj) % 2 == 1:
                pairs[i][j] = 1
                continue
            
            # If the guards have the same number of bananas, the game will 
            # definitely not loop infinitely. 
            if guardi == guardj:
                continue
            
            # In another case, if the number of bananas have differing powers of
            # 2 that can evenly divide them, that's also an infinite looping 
            # case.
            while guardi % 2 == 0 and guardj % 2 == 0:
                guardi /= 2
                guardj /= 2
            if guardi % 2 != guardj % 2:
                pairs[i][j] = 1
                continue
            
            # In a final case, we consider if the number of bananas have the
            # same powers of 2 that can evenly divide them. Keep dividing the
            # numbers by 2, multiplying the smaller number by 2, and subtracting
            # the smaller number from the larger number until one of two cases
            # happen: The sum becomes odd (infinite loop) or the guards have
            # the same number of bananas (no loop).
            while guardi != guardj and (guardi + guardj) % 2 != 1:
                    temp = max(guardi, guardj)
                    guardi = min(guardi, guardj)
                    guardj = temp - guardi
                    guardi *= 2
                    guardi /= 2
                    guardj /= 2                        
            if (guardi + guardj) % 2 == 1:
                pairs[i][j] = 1
                        
    # Now that we have which guard can be paired with which guard in order to
    # get an infinite loop, we can use a maximum matching algorithm to maximize
    # the number of guards we can distract, minimizing the number of guards that
    # will stand guard.
    return maximum_matching(pairs)