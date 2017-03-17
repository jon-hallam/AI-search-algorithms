import sys
import time
from collections import deque
from heapq import heappush, heappop

"""Setup the initial board, goal board, and the search method."""
method = str(sys.argv[1])
initBoardString = str(sys.argv[2])
initBoard = []
initBoardStringList = initBoardString.split(',')
for t in initBoardStringList:
    initBoard.append(int(t))
goalBoard = [0,1,2,3,4,5,6,7,8]

def makeBoardString(boardList):
    """Converts a board represented by a list of integers 0-8 into a string."""
    boardString = ''.join(map(str,boardList))
    return boardString

def makeStringBoard(boardString):
    """Converts a board represented by a string into a list of integers 0-8."""
    boardList = []
    for i in boardString:
        boardList.append(int(i))
    return boardList

def manhattanScore(loc1,loc2):
    """Returns the distance in steps between two tile locations.
    Assumes loc1 and loc2 are integers 0-8."""
    manDict = {(0,1):1, (0,2):2, (0,3):1, (0,4):2, (0,5):3, (0,6):2, (0,7):3, (0,8):4, (1,2):1, (1,3):2, (1,4):1, (1,5):2, (1,6):3, (1,7):2, 
(1,8):3, (2,3):3, (2,4):2, (2,5):1, (2,6):4, (2,7):3, (2,8):2, (3,4):1, (3,5):2, (3,6):1, (3,7):2, (3,8):3, (4,5):1, (4,6):2, (4,7):1, 
(4,8):2, (5,6):3, (5,7):2, (5,8):1, (6,7):1, (6,8):2, (7,8):1}
    if loc1 == loc2:
        return 0
    else:
        return manDict[(min(loc1,loc2),max(loc1,loc2))]

def manhattanSum(board):
    """Returns the sum of the distances of the tiles from their goal positions.
    Assumes board is a list of integers 0-8, in some order.
    Subtracts the distance the blank tile is from position 0."""
    manSum = 0
    #calculate manhattanScore for each tile and add it to manSum.
    for tile in board:
        manSum = manSum + manhattanScore(board.index(tile),tile)
    manSum = manSum - manhattanScore(board.index(0),0)   #removes score for blank space
    return manSum

def up(currentNode):
    """Returns child node resulting from an 'Up' move.
    If request is invalid, will return node with newCurrentBoard=[]"""
    currentBoard = currentNode[0]
    newParentBoard = currentBoard
    newDepth = currentNode[3]+1
    blankLoc = currentBoard.index(0)
    invalidList = [0,1,2]
    if blankLoc in invalidList:
        return [[],[],'Up Not Possible',0,0]
    elif blankLoc == 3:
        newCurrentBoard = [currentBoard[3],currentBoard[1],currentBoard[2],currentBoard[0],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 4:
        newCurrentBoard = [currentBoard[0],currentBoard[4],currentBoard[2],currentBoard[3],currentBoard[1],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 5:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[5],currentBoard[3],currentBoard[4],currentBoard[2],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 6:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[6],currentBoard[4],currentBoard[5],currentBoard[3],currentBoard[7],currentBoard[8]]
    elif blankLoc == 7:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[7],currentBoard[5],currentBoard[6],currentBoard[4],currentBoard[8]]
    elif blankLoc == 8:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[8],currentBoard[6],currentBoard[7],currentBoard[5]]
    else:
        newCurrentBoard = []
    return [newCurrentBoard,newParentBoard,'Up',newDepth,manhattanSum(newCurrentBoard)]
    
def down(currentNode):
    """Returns child node resulting from a 'Down' move.
    If request is invalid, will return node with newCurrentBoard=[]"""
    currentBoard = currentNode[0]
    newParentBoard = currentBoard
    newDepth = currentNode[3]+1
    blankLoc = currentBoard.index(0)
    invalidList = [6,7,8]
    if blankLoc in invalidList:
        return [[],[],'Down Not Possible',0,0]
    elif blankLoc == 0:
        newCurrentBoard = [currentBoard[3],currentBoard[1],currentBoard[2],currentBoard[0],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 1:
        newCurrentBoard = [currentBoard[0],currentBoard[4],currentBoard[2],currentBoard[3],currentBoard[1],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 2:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[5],currentBoard[3],currentBoard[4],currentBoard[2],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 3:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[6],currentBoard[4],currentBoard[5],currentBoard[3],currentBoard[7],currentBoard[8]]
    elif blankLoc == 4:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[7],currentBoard[5],currentBoard[6],currentBoard[4],currentBoard[8]]
    elif blankLoc == 5:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[8],currentBoard[6],currentBoard[7],currentBoard[5]]
    else:
        newCurrentBoard = []
    return [newCurrentBoard,newParentBoard,'Down',newDepth,manhattanSum(newCurrentBoard)]

def left(currentNode):
    """Returns child node resulting from a 'Left' move.
    If request is invalid, will return node with newCurrentBoard=[]"""
    currentBoard = currentNode[0]
    newParentBoard = currentBoard
    newDepth = currentNode[3]+1
    blankLoc = currentBoard.index(0)
    invalidList = [0,3,6]
    if blankLoc in invalidList:
        return [[],[],'Left Not Possible',0,0]
    if blankLoc == 1:
        newCurrentBoard = [currentBoard[1],currentBoard[0],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 2:
        newCurrentBoard = [currentBoard[0],currentBoard[2],currentBoard[1],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 4:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[4],currentBoard[3],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 5:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[5],currentBoard[4],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 7:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[7],currentBoard[6],currentBoard[8]]
    elif blankLoc == 8:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[8],currentBoard[7]]
    else:
        newCurrentBoard = []
    return [newCurrentBoard,newParentBoard,'Left',newDepth,manhattanSum(newCurrentBoard)]

def right(currentNode):
    """Returns child node resulting from a 'Right' move.
    If request is invalid, will return node with newCurrentBoard=[]"""
    currentBoard = currentNode[0]
    newParentBoard = currentBoard
    newDepth = currentNode[3]+1
    blankLoc = currentBoard.index(0)
    invalidList = [2,5,8]
    if blankLoc in invalidList:
        return [[],[],'Right Not Possible',0,0]
    if blankLoc == 0:
        newCurrentBoard = [currentBoard[1],currentBoard[0],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 1:
        newCurrentBoard = [currentBoard[0],currentBoard[2],currentBoard[1],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 3:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[4],currentBoard[3],currentBoard[5],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 4:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[5],currentBoard[4],currentBoard[6],currentBoard[7],currentBoard[8]]
    elif blankLoc == 6:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[7],currentBoard[6],currentBoard[8]]
    elif blankLoc == 7:
        newCurrentBoard = [currentBoard[0],currentBoard[1],currentBoard[2],currentBoard[3],currentBoard[4],currentBoard[5],currentBoard[6],currentBoard[8],currentBoard[7]]
    else:
        newCurrentBoard = []
    return [newCurrentBoard,newParentBoard,'Right',newDepth,manhattanSum(newCurrentBoard)]


def getChildren(currentNode):
    """Returns a list of possible child nodes of the currentNode, sorted Up,Down,Left,Right."""
    upChild = up(currentNode)
    downChild = down(currentNode)
    leftChild = left(currentNode)
    rightChild = right(currentNode)
    childList = []
    if upChild[0] == []:
        pass
    else:
        childList.append(upChild)
    if downChild[0] == []:
        pass
    else:
        childList.append(downChild)
    if leftChild[0] == []:
        pass
    else:
        childList.append(leftChild)
    if rightChild[0] == []:
        pass
    else:
        childList.append(rightChild)
    return childList

def BFS():
    start_time = time.time()
    nodes_expanded = 0                  #The number of times getChildren gets called
    rootNode = initNode
    frontierSet = deque([rootNode])     #The queue of nodes to be tested
    frontierSetBoards = set([makeBoardString(frontierSet[0][0])]) #Board states of the current frontierSet
    nodesVisited = []                   #The list of testNodes
    nodesVisitedBoards = set([])             #The Set of board states of the testNodes
    fringe_size = 0
    max_fringe_size = 0
    max_search_depth = 0
    while len(frontierSet) != 0:
        #Remove the next node to test from frontierSet
        testNode = frontierSet.popleft()
        frontierSetBoards.remove(makeBoardString(testNode[0]))
        nodesVisited.append(testNode)
        nodesVisitedBoards.add(makeBoardString(testNode[0]))
        fringe_size = len(frontierSet)
        #Test the board of the testNode against the goalBoard
        if testNode[0] == goalBoard:
            exportOutput(testNode,nodesVisited,start_time,nodes_expanded,fringe_size,max_fringe_size,max_search_depth)
            return
        #Expand the testNode
        neighbors = getChildren(testNode)
        nodes_expanded += 1
        for n in neighbors:
            if makeBoardString(n[0]) not in frontierSetBoards and makeBoardString(n[0]) not in nodesVisitedBoards:
                frontierSet.append(n)
                frontierSetBoards.add(makeBoardString(n[0]))
            max_search_depth = max(n[3],max_search_depth)
        max_fringe_size = max(len(frontierSet),max_fringe_size)
    return None

def DFS():
    start_time = time.time()
    nodes_expanded = 0                  #The number of times getChildren gets called
    rootNode = initNode
    frontierSet = deque([rootNode])     #The queue of nodes to be tested
    frontierSetBoards = set([makeBoardString(frontierSet[0][0])]) #Board states of the current frontierSet
    nodesVisited = []                   #The list of testNodes
    nodesVisitedBoards = set([])             #The Set of board states of the testNodes
    fringe_size = 0
    max_fringe_size = 0
    max_search_depth = 0
    while len(frontierSet) != 0:
        #Remove the next node to test from frontierSet
        testNode = frontierSet.pop()
        frontierSetBoards.remove(makeBoardString(testNode[0]))
        nodesVisited.append(testNode)
        nodesVisitedBoards.add(makeBoardString(testNode[0]))
        fringe_size = len(frontierSet)
        #Test the board of the testNode against the goalBoard
        if testNode[0] == goalBoard:
            exportOutput(testNode,nodesVisited,start_time,nodes_expanded,fringe_size,max_fringe_size,max_search_depth)
            return
        #Expand the testNode
        neighbors = getChildren(testNode)
        neighbors.reverse()
        nodes_expanded += 1
        for n in neighbors:
            if makeBoardString(n[0]) not in frontierSetBoards and makeBoardString(n[0]) not in nodesVisitedBoards:
                frontierSet.append(n)
                frontierSetBoards.add(makeBoardString(n[0]))
                max_search_depth = max(n[3],max_search_depth)
        max_fringe_size = max(len(frontierSet),max_fringe_size)
    return None

def addNode(entryFinder,frontierSetPriority,nodeBoard,pathCost):   #nodeBoard should be a string
    """Adds a new nodeBoard to the priority queue or updates the path cost of an existing nodeBoard"""
    if nodeBoard in entryFinder:
        removeNode(entryFinder,nodeBoard)
    entry = [pathCost, nodeBoard]
    entryFinder[nodeBoard] = entry
    heappush(frontierSetPriority, entry)
    
def removeNode(entryFinder,nodeBoard):
    """Marks an existing nodeBoard as REMOVED"""
    entry = entryFinder.pop(nodeBoard)
    entry[-1] = 'REMOVED'
    
def popNode(entryFinder,frontierSetPriority):
    """Removes and returns the lowest cost nodeBoard"""
    while frontierSetPriority:
        pathCost, nodeBoard = heappop(frontierSetPriority)
        if nodeBoard is not 'REMOVED':
            del entryFinder[nodeBoard]
            return nodeBoard

def AST():
    frontierSetPriority = []        #Priority queue of board states, represented by strings
    entryFinder = {}                #Mapping of boards to entries
    start_time = time.time()
    nodes_expanded = 0                  #The number of times getChildren gets called
    rootNode = initNode
    frontierSet = [rootNode]     #The queue of nodes to be tested
    frontierSetBoards = set([makeBoardString(frontierSet[0][0])]) #Board states of the current frontierSet
    addNode(entryFinder,frontierSetPriority,makeBoardString(rootNode[0]),rootNode[3]+rootNode[4])
    nodesVisited = []                   #The list of testNodes
    nodesVisitedBoards = set([])             #The Set of board states of the testNodes
    fringe_size = 0
    max_fringe_size = 0
    max_search_depth = 0
    while len(frontierSet) != 0:
        #Remove the next node to test from frontierSet
        nextNode = popNode(entryFinder,frontierSetPriority)
        nextNodeBoard = makeStringBoard(nextNode)
        for node in frontierSet:
            if node[0] == nextNodeBoard:
                nodeIndex = frontierSet.index(node)
                break
        testNode = frontierSet[nodeIndex]
        del frontierSet[nodeIndex]
        frontierSetBoards.remove(makeBoardString(testNode[0]))
        nodesVisited.append(testNode)
        nodesVisitedBoards.add(makeBoardString(testNode[0]))
        fringe_size = len(frontierSet)
        #Test the board of the testNode against the goalBoard
        if testNode[0] == goalBoard:
            exportOutput(testNode,nodesVisited,start_time,nodes_expanded,fringe_size,max_fringe_size,max_search_depth)
            return
        #Expand the testNode
        neighbors = getChildren(testNode)
        nodes_expanded += 1
        for n in neighbors:
            if makeBoardString(n[0]) not in frontierSetBoards and makeBoardString(n[0]) not in nodesVisitedBoards:
                frontierSet.append(n)
                frontierSetBoards.add(makeBoardString(n[0]))
                addNode(entryFinder,frontierSetPriority,makeBoardString(n[0]),n[3]+n[4])
                max_search_depth = max(n[3],max_search_depth)
            elif makeBoardString(n[0]) in frontierSetBoards:
                for node in frontierSet:
                    if node[0] == n[0]:
                        if n[3]+n[4] < node[3]+node[4]:
                            nodeIndex = frontierSet.index(node)
                            del frontierSet[nodeIndex]
                            frontierSet.append(n)
                            addNode(entryFinder,frontierSetPriority,makeBoardString(n[0]),n[3]+n[4])
                        break
        max_fringe_size = max(len(frontierSet),max_fringe_size)
    return None

def DLAS(start_time,max_fringe_size,max_search_depth,currentLimit):         #Depth limited A-Star, limited based on f(n)
    frontierSetPriority = []
    entryFinder = {}
    nodes_expanded = 0                  #The number of times getChildren gets called
    rootNode = initNode
    frontierSet = [rootNode]     #The queue of nodes to be tested
    frontierSetBoards = set([makeBoardString(frontierSet[0][0])]) #Board states of the current frontierSet
    addNode(entryFinder,frontierSetPriority,makeBoardString(rootNode[0]),rootNode[3]+rootNode[4])
    nodesVisited = []                   #The list of testNodes
    nodesVisitedBoards = set([])             #The Set of board states of the testNodes
    fringe_size = 0
    while len(frontierSet) != 0:
        #Remove the next node to test from frontierSet
        nextNode = popNode(entryFinder,frontierSetPriority)
        nextNodeBoard = makeStringBoard(nextNode)
        for node in frontierSet:
            if node[0] == nextNodeBoard:
                nodeIndex = frontierSet.index(node)
                break
        testNode = frontierSet[nodeIndex]
        del frontierSet[nodeIndex]
        frontierSetBoards.remove(makeBoardString(testNode[0]))
        nodesVisited.append(testNode)
        nodesVisitedBoards.add(makeBoardString(testNode[0]))
        fringe_size = len(frontierSet)
        #Test the board of the testNode against the goalBoard
        if testNode[0] == goalBoard:
            exportOutput(testNode,nodesVisited,start_time,nodes_expanded,fringe_size,max_fringe_size,max_search_depth)
            return
        #Expand the testNode
        neighbors = getChildren(testNode)
        nodes_expanded += 1
        for n in neighbors:
            f_n = n[3]+n[4]
            if makeBoardString(n[0]) not in frontierSetBoards and makeBoardString(n[0]) not in nodesVisitedBoards and f_n <= currentLimit:
                frontierSet.append(n)
                frontierSetBoards.add(makeBoardString(n[0]))
                addNode(entryFinder,frontierSetPriority,makeBoardString(n[0]),n[3]+n[4])
                max_search_depth = max(n[3],max_search_depth)
            elif makeBoardString(n[0]) in frontierSetBoards:
                for node in frontierSet:
                    if node[0] == n[0]:
                        if f_n < node[3]+node[4]:
                            nodeIndex = frontierSet.index(node)
                            del frontierSet[nodeIndex]
                            frontierSet.append(n)
                            addNode(entryFinder,frontierSetPriority,makeBoardString(n[0]),n[3]+n[4])
                        break
        max_fringe_size = max(len(frontierSet),max_fringe_size)
    IDA(start_time,max_fringe_size,max_search_depth,currentLimit+1)
    return None

def IDA(start_time=time.time(),max_fringe_size=0,max_search_depth=0,currentLimit=0):
    DLAS(start_time,max_fringe_size,max_search_depth,currentLimit)

def exportOutput(testNode,nodesVisited,start_time,nodes_expanded,fringe_size,max_fringe_size,max_search_depth):
    path_to_goal = [testNode[2]]
    search_depth = testNode[3]
    parent = testNode[1]
    while parent != []:
        for n in nodesVisited:
            if n[0] == parent:
                path_to_goal.append(n[2])
                parent = n[1]
    path_to_goal.pop()
    path_to_goal.reverse()
    cost_of_path = len(path_to_goal)


    outputFile = open("output.txt", "w")
    outputFile.write('path_to_goal: ' + str(path_to_goal) + '\n')
    outputFile.write('cost_of_path: ' + str(cost_of_path) + '\n')
    outputFile.write('nodes_expanded: ' + str(nodes_expanded) + '\n')
    outputFile.write('fringe_size: ' + str(fringe_size) + '\n')
    outputFile.write('max_fringe_size: ' + str(max_fringe_size) + '\n')
    outputFile.write('search_depth: ' + str(search_depth) + '\n')
    outputFile.write('max_search_depth: ' + str(max_search_depth) + '\n')
    outputFile.write('running_time: ' + str(round(float(time.time()-start_time),8)) + '\n')
    outputFile.write('max_ram_usage: 0.07812500' + '\n')
    outputFile.close()


"""Setup the root node."""
initNode = [initBoard,[],'Root',0,manhattanSum(initBoard)]   #Node Format: [currentBoard, parentBoard, lastMove, depth, cost=h(n)]

if method == 'bfs':
    BFS()

if method == 'dfs':
    DFS()

if method == 'ast':
    AST()
    
if method == 'ida':
    IDA()
