# term-project.py

# Name: Carina Sanborn
# Andrew ID: czsanbor

import random, copy
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

def appStarted(app):
    app.islands = dict()
    app.bridges = set()
    app.boardSize = 7
    app.board = [ ([None] * app.boardSize) for row in range(app.boardSize)] #7x7 empty board
    app.currentIslands = dict()
    app.currentBoard = [ ([None] * app.boardSize) for row in range(app.boardSize)]
    app.boardWidth = 400
    app.lrMargin = 200
    app.udMargin = 100
    app.cellSize = 400//app.boardSize
    app.startScreen = True
    app.practice1Screen = False
    app.practice2Screen = False
    app.practice3Screen = False
    app.randomBoardScreen = False
    app.instructionsScreen = False
    app.helpScreen = False
    app.instructions = instructions()
    app.helpScreenInstructions = helpScreenInstructions()
    app.firstIslandPressed = None
    app.boardSolved = None
    app.previousScreen = None

# https://www.conceptispuzzles.com/index.aspx?uri=puzzle/hashi/rules
def instructions():
    instructions = '''
                    Islands and Bridges (aka Hashi) is a logic puzzle game 
                    invented in Japan. The object of the game is to connect 
                    all the islands with bridges. 
                      
                      * Each island has a number that represents the number of 
                        bridges it must have
                      * An island cannot have more than two bridges in the same
                        direction
                      * Bridges can only be horizontal or vertical  
                      * Bridges cannot cross over islands or other bridges
                      
                    The puzzle is solved once all the islands are connected 
                    and each island has the correct number of bridges.
                    '''
    return instructions

def helpScreenInstructions():
    instructions = '''
                    * to create a bridge between two islands click on an island 
                      and then click on the island you want it to connect to
                    * when you click on an island all the possible islands you 
                      can connect to will highlight yellow
                    * you cannot create a bridge between two islands that are 
                      touching eachother
                    * clicking on a single bridge will turn it into a double bridge
                    * clicking on a double bridge will delete the bridge  
                    * once an island has the correct number of bridges it will
                      turn green, however, just because an island has the correct
                      number of bridges does not mean it is correct
                    * if an island has too many bridges it will turn red
                    * if you need help getting started click the 'Get Hint' Button
                    * if you want to see the solution click the 'See Solution' Button
                    * to reset the board click the 'Reset' Button
                    * once you believe you are finished, click the 'Finish' Button
                      to check if you solved the puzzle correctly
                   ''' 
    return instructions

#From puzzle-bridges.com 
#Puzzle ID: 9,954,585
def practice2Board():
    board = {(0,0): [(0,4), (4,0), (4,0)],
             (0,4): [(0,0), (0,6), (0,6), (5,4)],
             (0,6): [(0,4), (0,4), (3,6)],
             (1,1): [(1,3), (1,3), (5,1), (5,1)],
             (1,3): [(1,1), (1,1), (4,3), (4,3)],
             (3,6): [(0,6), (5,6)],
             (4,0): [(0,0), (0,0), (6,0), (6,0)],
             (4,3): [(1,3), (1,3)],
             (5,1): [(1,1), (1,1), (5,4), (5,4)],
             (5,4): [(5,1), (5,1), (0,4), (5,6), (5,6)],
             (5,6): [(5,4), (5,4), (3,6)],
             (6,0): [(4,0), (4,0), (6,2)],
             (6,2): [(6,0)]
             }
    return board

#From puzzle-bridges.com 
#Puzzle ID: 1,583,991
def practice1Board():
    board = {(0,0): [(0,4), (0,4), (3,0)],
             (0,4): [(0,0), (0,0), (0,6), (0,6), (4,4)],
             (0,6): [(0,4), (0,4), (4,6), (4,6)],
             (3,0): [(0,0), (3,3)],
             (3,3): [(3,0)],
             (4,2): [(4,4), (4,4)],
             (4,4): [(4,2), (4,2), (0,4), (4,6), (6,4), (6,4)],
             (4,6): [(4,4), (0,6), (0,6), (6,6)],
             (6,0): [(6,2)],
             (6,2): [(6,0), (6,4)],
             (6,4): [(6,2), (4,4), (4,4), (6,6), (6,6)],
             (6,6): [(6,4), (6,4), (4,6)]
            }
    return board

#From puzzle-bridges.com
#Puzzle ID: 4,252,492
def practice3Board():
    board = {(0,0): [(0,2), (3,0)],
             (0,2): [(0,0), (0,4), (3,2), (3,2)],
             (0,4): [(0,2)],
             (0,6): [(4,6), (4,6)],
             (2,4): [(4,4)],
             (3,0): [(0,0), (3,2), (3,2), (6,0), (6,0)],
             (3,2): [(3,0), (3,0), (0,2), (0,2)],
             (4,1): [(4,4), (4,4)],
             (4,4): [(4,1), (4,1), (2,4), (4,6), (4,6), (6,4), (6,4)],
             (4,6): [(4,4), (4,4), (0,6), (0,6), (6,6)],
             (6,0): [(3,0), (3,0), (6,2)],
             (6,2): [(6,0), (6,4), (6,4)],
             (6,4): [(6,2), (6,2), (4,4), (4,4), (6,6), (6,6)],
             (6,6): [(6,4), (6,4), (4,6)]
            }
    return board

def mousePressed(app, event):
    if app.startScreen:
        if ((app.width//2 - 240 < event.x < app.width//2 - 20) and 
            (app.height//3 - 50 < event.y < app.height//3 + 50)):
            #generate board 7 x 7 button pressed
            app.startScreen = False
            app.randomBoardScreen = True
            generateBoard(app)
            generateBlankBoard(app)
        elif ((app.width//2 + 20 < event.x < app.width + 240) and
              (app.height//3 - 50 < event.y < app.height//3 + 50)):
            #generate board 9 x x9 button pressed
            app.startScreen = False
            app.randomBoardScreen = True
            app.boardSize = 9
            app.board = [ ([None] * app.boardSize) for row in range(app.boardSize)]
            app.currentBoard = [ ([None] * app.boardSize) for row in range(app.boardSize)]
            app.cellSize = app.boardWidth//app.boardSize
            generateBoard(app)
            generateBlankBoard(app)
        elif((app.width//5 - 90 < event.x < app.width//5 + 90) and
            (2*app.height//3 - 50 < event.y < 2*app.height//3 + 50)):
            #practice 1 button pressed
            app.startScreen = False
            app.practice1Screen = True
            app.islands = practice1Board()
            generateBlankBoard(app)
        elif((app.width//2 - 90 < event.x < app.width//2 + 90) and 
            (2*app.height//3 - 50 < event.y < 2*app.height//3 + 50)):
            #practice 2 button pressed
            app.startScreen = False
            app.practice2Screen = True
            app.islands = practice2Board()
            generateBlankBoard(app)
        elif((4*app.width//5 - 90 < event.x < 4*app.width//5 + 90)and
            (2*app.height//3 - 50 < event.y < 2*app.height//3 + 50)):
            #practice 3 button pressed
            app.startScreen = False
            app.practice3Screen = True
            app.islands = practice3Board()
            generateBlankBoard(app)
        elif((app.width//2 - 60 < event.x < app.width//2 + 60) and
            (6*app.height//7 - 30 < event.y < 6*app.height//7 + 30)):
            #instructions button pressed
            app.startScreen = False
            app.instructionsScreen = True
    elif app.helpScreen:
        if (30 < event.x < 100) and (app.height - 80 < event.y < app.height - 30):
            #back button pressed
            app.helpScreen = False
            if app.previousScreen == "practice1":
                app.practice1Screen = True
            elif app.previousScreen == "practice2":
                app.practice2Screen = True
            elif app.previousScreen == "practice3":
                app.practice3Screen = True
            elif app.previousScreen == "randomBoard":
                app.randomBoardScreen = True
            app.previousScreen = None
    else:
        if (30 < event.x < 100) and (app.height - 80 < event.y < app.height - 30):
            #back button pressed
            appStarted(app)
        elif app.boardSolved == True:
            if app.boardSize == 9:
                appStarted(app)
                app.startScreen = False
                app.randomBoardScreen = True
                app.boardSize = 9
                app.board = [ ([None] * app.boardSize) for row in range(app.boardSize)]
                app.currentBoard = [ ([None] * app.boardSize) for row in range(app.boardSize)]
                app.cellSize = app.boardWidth//app.boardSize
                generateBoard(app)
                generateBlankBoard(app)
            elif app.practice1Screen:
                appStarted(app)
                app.startScreen = False
                app.practice2Screen = True
                app.islands = practice2Board()
                generateBlankBoard(app)
            elif app.practice2Screen:
                appStarted(app)
                app.startScreen = False
                app.practice3Screen = True
                app.islands = practice3Board()
                generateBlankBoard(app)
            else:
                appStarted(app)
                app.startScreen = False
                app.randomBoardScreen = True
                generateBoard(app)
                generateBlankBoard(app)
        elif (125 < event.x < 255) and (app.height - 80 < event.y < app.height - 30):
            #see solution button pressed
            resetBoard(app)
            app.currentIslands = app.islands
            app.boardSolved = True
        elif (265 < event.x < 395) and (app.height - 80 < event.y < app.height - 30):
            #get hint button pressed
            resetBoard(app)
            giveHint(app)
        elif (405 < event.x < 535) and (app.height - 80 < event.y < app.height - 30): 
            #reset button pressed
            resetBoard(app) 
        elif (545 < event.x < 675) and (app.height - 80 < event.y < app.height - 30):
            #finish button pressed
            if checkIfBoardIsCorrect(app):
                app.boardSolved = True
            else:
                app.boardSolved = False
        elif (app.width - 100 < event.x < app.width - 30) and (app.height - 80 < event.y < app.height - 30):
            #help button pressed
            if app.practice1Screen:
                app.practice1Screen = False
                app.previousScreen = "practice1"
                app.helpScreen = True
            elif app.practice2Screen:
                app.practice2Screen = False
                app.previousScreen = "practice2"
                app.helpScreen = True
            elif app.practice3Screen:
                app.practice3Screen = False
                app.previousScreen = "practice3"
                app.helpScreen = True
            elif app.randomBoardScreen:
                app.randomBoardScreen = False
                app.previousScreen = "randomBoard"
                app.helpScreen = True
        elif ((app.width//2 - 200 < event.x < app.width//2 + 200) and 
              (app.height//2 - 200 < event.y < app.height//2 + 200)):
            #cell on board was pressed
            cell = getCell(app, event.x, event.y)
            if app.currentBoard[cell[0]][cell[1]] == "Bridge":
                island1, island2 = getIslandsFromBridge(app, cell)
                if app.currentIslands[island1].count(island2) == 2:
                    app.currentIslands[island1].remove(island2)
                    app.currentIslands[island2].remove(island1)
                    app.currentIslands[island1].remove(island2)
                    app.currentIslands[island2].remove(island1)
                    removeBridgeFromCurrentBoard(app, island1, island2)
                else:
                    app.currentIslands[island1] += [island2]
                    app.currentIslands[island2] += [island1]
                    addBridgeToCurrentBoard(app, island1, island2)
                app.firstIslandPressed == None
            elif cell in app.islands:
                if app.firstIslandPressed == None:
                    app.firstIslandPressed = cell
                elif app.firstIslandPressed == cell:
                    app.firstIslandPressed = None
                else:
                    if bridgeIsValid(app, cell, app.firstIslandPressed):
                        if app.currentIslands[app.firstIslandPressed].count(cell) == 2:
                           app.currentIslands[app.firstIslandPressed].remove(cell)
                           app.currentIslands[app.firstIslandPressed].remove(cell)
                           app.currentIslands[cell].remove(app.firstIslandPressed)
                           app.currentIslands[cell].remove(app.firstIslandPressed)
                           removeBridgeFromCurrentBoard(app, cell, app.firstIslandPressed)
                        else:
                            app.currentIslands[app.firstIslandPressed] += [cell]
                            app.currentIslands[cell] += [app.firstIslandPressed]
                            addBridgeToCurrentBoard(app, cell, app.firstIslandPressed)
                    app.firstIslandPressed = None

################################################################################
# User Interacting with Board
################################################################################
def bridgeIsValid(app, island1, island2):
    if island1[0] == island2[0]: #same row
        row = island1[0]
        if island1[1] < island2[1]:
            if island1[1] + 1 == island2[1]:
                return False
            for col in range(island1[1] + 1, island2[1]):
                if app.currentBoard[row][col] == "Island":
                    return False
        else:
            if island2[1] + 1 == island1[1]:
                return False
            for col in range(island2[1] + 1, island1[1]):
                if app.currentBoard[row][col] == "Island":
                    return False
        return True
    elif island1[1] == island2[1]: #same col
        col = island1[1]
        if island1[0] < island2[0]:
            if island1[0] + 1 == island2[0]:
                return False
            for row in range(island1[0] + 1, island2[0]):
                if app.currentBoard[row][col] == "Island":
                    return False
        else:
            if island2[0] + 1 == island1[0]:
                return False
            for row in range(island2[0] + 1, island2[0]):
                if app.currentBoard[row][col] == "Island":
                    return False
        return True
    return False #not the same row or col

def addBridgeToCurrentBoard(app, island1, island2):
    if island1[0] == island2[0]:
        row = island1[0]
        if island1[1] > island2[1]:
            for col in range(island2[1] + 1, island1[1]):
                app.currentBoard[row][col] = "Bridge"
        else:
            for col in range(island1[1] + 1, island2[1]):
                app.currentBoard[row][col] = "Bridge"
    else:
        col = island1[1]
        if island1[0] > island2[0]:
            for row in range(island2[0] + 1, island1[0]):
                app.currentBoard[row][col] = "Bridge"
        else:
            for row in range(island1[0] + 1, island2[0]):
                app.currentBoard[row][col] = "Bridge"

def removeBridgeFromCurrentBoard(app, island1, island2):
    if island1[0] == island2[0]:
        row = island1[0]
        if island1[1] > island2[1]:
            for col in range(island2[1] + 1, island1[1]):
                app.currentBoard[row][col] = None
        else:
            for col in range(island1[1] + 1, island2[1]):
                app.currentBoard[row][col] = None
    else:
        col = island1[1]
        if island1[0] > island2[0]:
            for row in range(island2[0] + 1, island1[0]):
                app.currentBoard[row][col] = None
        else:
            for row in range(island1[0] + 1, island2[0]):
                app.currentBoard[row][col] = None

def getIslandsFromBridge(app, cell):
    bridgeRow = cell[0]
    bridgeCol = cell[1]
    island1 = None
    island2 = None
    for col in range(bridgeCol - 1, -1, -1):
        if app.currentBoard[bridgeRow][col] == "Island": #check for island to the left
            island1 = (bridgeRow, col)
            break
    if island1 != None:
        for col in range(bridgeCol + 1, app.boardSize, 1):
            if app.currentBoard[bridgeRow][col] == "Island": #check for island to the right
                island2 = (bridgeRow,col)
                break
        if island2 != None:
            if island2 in app.currentIslands[island1]: #bridge between island1 and island2
                return island1, island2
    island1 = None
    island2 = None
    for row in range(bridgeRow - 1, -1, -1):
        if app.currentBoard[row][bridgeCol] == "Island": #check for island above
            island1 = (row, bridgeCol)
            break
    if island1 != None:
        for row in range(bridgeRow + 1, app.boardSize, 1):
            if app.currentBoard[row][bridgeCol] == "Island": #check for bridge below
                island2 = (row, bridgeCol)
                break
        if island2 != None:
            if island2 in app.currentIslands[island1]: #bridge between island1 and island2
                return island1, island2

################################################################################
# Checking if Board is Correct
################################################################################
def checkIfBoardIsCorrect(app):
    for island in app.currentIslands:
        if len(app.currentIslands[island]) != len(app.islands[island]):
            return False
    node = list(app.currentIslands.keys())[0]
    islandsVisited = [node]
    return set(app.islands.keys()) == set(checkIfBoardIsCorrectFromNode(app, node, islandsVisited))

def checkIfBoardIsCorrectFromNode(app, node, islandsVisited):
    for island in set(app.currentIslands[node]):
        if island not in islandsVisited:
            islandsVisited += [island]
            checkIfBoardIsCorrectFromNode(app, island, islandsVisited)
    return islandsVisited

################################################################################
# First attempt at solving board with backtracking (Does not work)
################################################################################
def solveBoard(app):
    node = list(app.currentIslands.keys())[0]
    islandsVisited = [node]
    adjacentNodes = getAdjacentNodes(app, node)
    possibleBridgeCombs = getPossibleBridgeCombs(app, node)
    for comb in possibleBridgeCombs:
        if solveBoardWithComb(app, node, comb, adjacentNodes, islandsVisited):
            return

def solveBoardWithComb(app, node, comb, adjacentNodes, islandsVisited):
    previousCurrentIslands = app.currentIslands.copy()
    previousIslandsVisited = copy.copy(islandsVisited)
    print(node)
    print(comb, adjacentNodes)
    #add bridge comb to current islands
    for i in range(len(comb)):
        if comb[i] != 0: #if comb[i] == 0 the node and adjacentNodes[i] don't connect
            app.currentIslands[node] += [adjacentNodes[i]]*comb[i]
            app.currentIslands[adjacentNodes[i]] += [node]*comb[i]
            if adjacentNodes[i] in islandsVisited: #cycle
                if len(app.currentIslands[adjacentNodes[i]]) != len(app.islands[adjacentNodes[i]]):
                    app.currentIslands = previousCurrentIslands
                    islandsVisited = previousIslandsVisited
                    return False
            else:
                possibleBridgeCombs = getPossibleBridgeCombs(app, adjacentNodes[i])
                if possibleBridgeCombs == [] and len(app.currentIslands[adjacentNodes[i]]) != len(app.islands[adjacentNodes[i]]):
                    app.currentIslands = previousCurrentIslands.copy()
                    islandsVisited = copy.copy(previousIslandsVisited)
                    return False
                else:
                    islandsVisited += [adjacentNodes[i]]
                    nextAdjacentNodes1 = getAdjacentNodes(app, adjacentNodes[i])
                    nextAdjacentNodes2 = []
                    for island in nextAdjacentNodes1:
                        if island not in app.currentIslands[adjacentNodes[i]]:
                            nextAdjacentNodes2 += [island]
                    if nextAdjacentNodes2 == []:
                        continue
                    for comb in possibleBridgeCombs:
                        if solveBoardWithComb(app, adjacentNodes[i], comb, nextAdjacentNodes2, islandsVisited):
                            return True
    if checkIfBoardIsCorrect(app):
        return True

################################################################################
# Second attempt at solving board (give hint)
################################################################################
def giveHint(app):
    bridgesAdded = False
    for node in app.currentIslands:
        adjacentNodes = getAdjacentNodes(app, node)
        possibleBridgeCombs = getPossibleBridgeCombs(app, node)
        if len(possibleBridgeCombs) == 1:
            bridgesAdded = True
            comb = possibleBridgeCombs[0]
            for i in range(len(comb)):
                if comb[i] != 0:
                    app.currentIslands[node] += [adjacentNodes[i]]*comb[i]
                    app.currentIslands[adjacentNodes[i]] += [node]*comb[i]
                    addBridgeToCurrentBoard(app, node, adjacentNodes[i])
    if bridgesAdded == False:
        for node in app.currentIslands:
            adjacentNodes = getAdjacentNodes(app, node)
            possibleBridgeCombs = getPossibleBridgeCombs(app, node)
            if zeroNotInBridgeCombs(app, possibleBridgeCombs):
                for adjacentNode in adjacentNodes:
                    app.currentIslands[node] += [adjacentNode]
                    app.currentIslands[adjacentNode] += [node]
                    addBridgeToCurrentBoard(app, node, adjacentNode)

################################################################################
# Helper Functions
################################################################################
def getPossibleBridgeCombs(app, node):
    possibleCombinations = []
    adjacentNodes = getAdjacentNodes(app, node)
    numBridges = len(app.islands[node])
    if len(app.currentIslands[node]) == numBridges:
        return []
    elif len(adjacentNodes) == 1:
        for num1 in range(3):
            if num1 + len(app.currentIslands[node]) == numBridges:
                possibleCombinations += [(num1,)]
    elif len(adjacentNodes) == 2:
        for num1 in range(3):
            for num2 in range(3):
                if num1 + num2 + len(app.currentIslands[node]) == numBridges:
                    possibleCombinations += [(num1, num2)]
    elif len(adjacentNodes) == 3:
        for num1 in range(3):
            for num2 in range(3):
                for num3 in range(3):
                    if num1 + num2 + num3 + len(app.currentIslands[node]) == numBridges:
                        possibleCombinations += [(num1, num2, num3)]
    elif len(adjacentNodes) == 4:
        for num1 in range(3):
            for num2 in range(3):
                for num3 in range(3):
                    for num4 in range(3):
                        if num1 + num2 + num3 + num4 + len(app.currentIslands[node]) == numBridges:
                            possibleCombinations += [(num1, num2, num3, num4)]
    return possibleCombinations

def zeroNotInBridgeCombs(app, bridgeCombs):
    if bridgeCombs == []:
        return False
    for comb in bridgeCombs:
        if 0 in comb:
            return False
    return True

def getAdjacentNodes(app, node):
    adjacentNodes = []
    nodeRow = node[0]
    nodeCol = node[1]
    for dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
        if dir == "UP":
            for row in range(nodeRow - 1, -1, -1):
                if app.currentBoard[nodeRow - 1][nodeCol] == "Island":
                    break
                elif app.currentBoard[row][nodeCol] == "Island":
                    adjacentNodes += [(row, nodeCol)]
                    break 
        elif dir == "DOWN":
            for row in range(nodeRow + 1, app.boardSize, 1):
                if app.currentBoard[nodeRow + 1][nodeCol] == "Island":
                    break
                elif app.currentBoard[row][nodeCol] == "Island":
                    adjacentNodes += [(row, nodeCol)]
                    break
        elif dir == "LEFT":
            for col in range(nodeCol - 1, -1, -1):
                if app.currentBoard[nodeRow][nodeCol - 1] == "Island":
                    break
                elif app.currentBoard[nodeRow][col] == "Island":
                    adjacentNodes += [(nodeRow, col)]
                    break
        elif dir == "RIGHT":
            for col in range(nodeCol + 1, app.boardSize, 1):
                if app.currentBoard[nodeRow][nodeCol + 1] == "Island":
                    break
                elif app.currentBoard[nodeRow][col] == "Island":
                    adjacentNodes += [(nodeRow, col)]
                    break
    adjacentNodes1 =[]
    for adjacentNode in adjacentNodes:
        if checkForBridgeBetweenNodes(app, node, adjacentNode) == False: #there is not a bridge separating the islands
            adjacentNodes1 += [adjacentNode]
    adjacentNodes2 = []
    for adjacentNode in adjacentNodes1:
        if (len(app.currentIslands[adjacentNode]) < len(app.islands[adjacentNode]) and 
        app.currentIslands[node].count(adjacentNode) < 2):
            #adjacentNode is not already full and the islands do not have the maximum number of bridges
            adjacentNodes2 += [adjacentNode]
    return adjacentNodes2

def checkForBridgeBetweenNodes(app, island1, island2):
    if island2 in app.currentIslands[island1]: #the islands are already connected
        return False
    else:
        if island1[0] == island2[0]:
            row = island1[0]
            if island1[1] > island2[1]:
                for col in range(island2[1] + 1, island1[1]):
                    if app.currentBoard[row][col] == "Bridge":
                        return True
            else:
                for col in range(island1[1] + 1, island2[1]):
                    if app.currentBoard[row][col] == "Bridge":
                        return True
        else:
            col = island1[1]
            if island1[0] > island2[0]:
                for row in range(island2[0] + 1, island1[0]):
                    if app.currentBoard[row][col] == "Bridge":
                        return True
            else:
                for row in range(island1[0] + 1, island2[0]):
                    if app.currentBoard[row][col] == "Bridge":
                        return True
    return False

###############################################################################
# Buttons
###############################################################################   
def drawGenerate7x7BoardButton(app, canvas):
    canvas.create_rectangle(app.width//2 - 240, app.height//3 - 50, app.width//2
                        - 20, app.height//3 + 50, width= 5)
    canvas.create_text(app.width//2 - 130, app.height//3 - 15, text= "Generate Board",
                        font= "Ariel 20 bold")
    canvas.create_text(app.width//2 - 130, app.height//3 + 15, text= "7 x 7",
                        font= "Ariel 20 bold")
                    
def drawGenerate9x9BoardButton(app, canvas):
    canvas.create_rectangle(app.width//2 + 20, app.height//3 - 50, app.width//2
                        + 240, app.height//3 + 50, width= 5)
    canvas.create_text(app.width//2 + 130, app.height//3 - 15, text= "Generate Board",
                        font= "Ariel 20 bold")
    canvas.create_text(app.width//2 + 130, app.height//3 + 15, text= "9 x 9",
                        font= "Ariel 20 bold")

def drawPractice1Button(app, canvas):
    canvas.create_rectangle(app.width//5 - 90, 2*app.height//3 - 50, 
                        app.width//5 + 90, 2*app.height//3 + 50, width= 5)
    canvas.create_text(app.width//5, 2*app.height//3, text= "Practice 1",
                        font= "Ariel 20 bold")

def drawPractice2Button(app, canvas):
    canvas.create_rectangle(app.width//2 - 90, 2*app.height//3 - 50, 
                        app.width//2 + 90, 2*app.height//3 +50, width= 5)
    canvas.create_text(app.width//2, 2*app.height//3, text= "Practice 2",
                        font= "Ariel 20 bold")

def drawPractice3Button(app, canvas):
    canvas.create_rectangle(4*app.width//5 - 90, 2*app.height//3 - 50, 
                        4*app.width//5 + 90, 2*app.height//3 +50, width= 5)
    canvas.create_text(4*app.width//5, 2*app.height//3, text= "Practice 3",
                        font= "Ariel 20 bold")

def drawInstuctionsButton(app, canvas):
    canvas.create_rectangle(app.width//2 - 60, 6*app.height//7 - 30,
                        app.width//2 + 60, 6*app.height//7 + 30, width= 5)
    canvas.create_text(app.width//2, 6*app.height//7, text= "Instructions",
                        font= "Ariel 12 bold")

def drawBackButton(app, canvas):
    canvas.create_rectangle(30, app.height - 80, 100, app.height - 30, width= 4)
    canvas.create_text(65, app.height - 55, text= "Back", font= "Ariel 14 bold")

def drawSeeSolutionButton(app, canvas):
    canvas.create_rectangle(125, app.height - 80, 255,
                        app.height - 30, width= 4)
    canvas.create_text(190, app.height - 55, text= "See Solution", 
                        font= "Ariel 14 bold")

def drawGetHintButton(app, canvas):
    canvas.create_rectangle(265, app.height - 80, 395,
                        app.height - 30, width= 4)
    canvas.create_text(330, app.height - 55, text= "Get Hint", 
                        font= "Ariel 14 bold")

def drawResetButton(app, canvas):
    canvas.create_rectangle(405, app.height - 80, 535,
                        app.height - 30, width= 4)
    canvas.create_text(470, app.height - 55, text= "Reset Board", 
                        font= "Ariel 14 bold")

def drawFinishButton(app, canvas):
    canvas.create_rectangle(545, app.height - 80, 675,
                        app.height - 30, width= 4)
    canvas.create_text(610, app.height - 55, text= "Finish", 
                        font= "Ariel 14 bold")

def drawHelpButton(app, canvas):
    canvas.create_rectangle(app.width - 100, app.height - 80, app.width - 30, app.height - 30, width= 4)
    canvas.create_text(app.width - 65, app.height - 55, text= "Help", font= "Ariel 14 bold")

def drawButtons(app, canvas):
    drawBackButton(app, canvas)
    drawSeeSolutionButton(app, canvas)
    drawGetHintButton(app, canvas)
    drawResetButton(app, canvas)
    drawFinishButton(app, canvas)
    drawHelpButton(app, canvas)
    
###############################################################################
# Screens
###############################################################################
def drawStartScreen(app, canvas):
    canvas.create_text(app.width//2, 50, text= "Islands and Bridges", font= 
                        "Ariel 30 bold")
    drawGenerate7x7BoardButton(app, canvas)
    drawGenerate9x9BoardButton(app, canvas)
    drawPractice1Button(app, canvas)
    drawPractice2Button(app, canvas)
    drawPractice3Button(app, canvas)
    drawInstuctionsButton(app, canvas)

def drawPractice1Screen(app, canvas):
    canvas.create_text(app.width//2, 40, text= "Practice 1", font= 
                        "Ariel 30 bold")
    drawBoard(app, canvas)
    drawButtons(app, canvas)
    if app.boardSolved == True:
        canvas.create_text(app.width//2, 70, text= "Well Done! Click to move to Practice 2!",
                        font= "Ariel 15 bold", fill= "Green")
    elif app.boardSolved == False:
        canvas.create_text(app.width//2, 70, text= "Not Quite. Keep Trying!", font= "Ariel 15 bold",
                        fill= "Red")

def drawPractice2Screen(app, canvas):
    canvas.create_text(app.width//2, 40, text= "Practice 2", font= 
                        "Ariel 30 bold")
    drawBoard(app, canvas)
    drawButtons(app, canvas)
    if app.boardSolved == True:
        canvas.create_text(app.width//2, 70, text= "Well Done! Click to move to Practice 3!",
                        font= "Ariel 15 bold", fill= "Green")
    elif app.boardSolved == False:
        canvas.create_text(app.width//2, 70, text= "Not Quite. Keep Trying!", font= "Ariel 15 bold",
                        fill= "Red")

def drawPractice3Screen(app, canvas):
    canvas.create_text(app.width//2, 40, text= "Practice 3", font= 
                        "Ariel 30 bold")
    drawBoard(app, canvas)
    drawButtons(app, canvas)
    if app.boardSolved == True:
        canvas.create_text(app.width//2, 70, text= "Well Done! Click to generate new board!",
                        font= "Ariel 15 bold", fill= "Green")
    elif app.boardSolved == False:
        canvas.create_text(app.width//2, 70, text= "Not Quite. Keep Trying!", font= "Ariel 15 bold",
                        fill= "Red")

def drawRandomBoardScreen(app, canvas):
    canvas.create_text(app.width//2, 40, text= "Islands and Bridges", font= 
                        "Ariel 30 bold")
    drawBoard(app, canvas)
    drawButtons(app, canvas)
    if app.boardSolved == True:
        canvas.create_text(app.width//2, 70, text= "Well Done! Click to generate new board!",
                        font= "Ariel 15 bold", fill= "Green")
    elif app.boardSolved == False:
        canvas.create_text(app.width//2, 70, text= "Not Quite. Keep Trying!", font= "Ariel 15 bold",
                        fill= "Red")

def drawInstructionsScreen(app, canvas):
    canvas.create_text(app.width//2, 50, text= "Instructions", font= 
                        "Ariel 30 bold")
    canvas.create_text(app.width//2, app.height//2, text= app.instructions, 
                        font= "Ariel 15")
    drawBackButton(app, canvas)

def drawHelpScreen(app, canvas):
    canvas.create_text(app.width//2, 50, text= "Help", font= 
                        "Ariel 30 bold")
    canvas.create_text(app.width//2, app.height//2, text= app.helpScreenInstructions, 
                        font= "Ariel 15")
    drawBackButton(app, canvas)


###############################################################################
# Generating Board
###############################################################################
def generateBoard(app):
    # find a random row and col to start the board from 
    row = random.randint(0, app.boardSize - 1)
    col = random.randint(0, app.boardSize - 1)
    app.board[row][col] = "Island"
    app.islands[(row, col)] = []
    generateBoardFromNode(app, (row, col), 0)

def generateBoardFromNode(app, node, depth):
    if len(app.islands) > 12 and app.boardSize == 7:
        return
    elif len(app.islands) > 20 and app.boardSize == 9:
        return
    else:
        #generate adjacent nodes in each direction
        for dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
            #will there be an adjacent node in this direction(0=False, 1,2=True)
            adjacentNode = random.randint(0, 2)
            if depth < 4 or adjacentNode == 1 or adjacentNode == 2:
                possiblePositions = getPossibleNewNodePositions(app, node, dir)
                if possiblePositions != []:
                    newNode = random.choice(possiblePositions)
                    newNodeRow = newNode[0]
                    newNodeCol = newNode[1]
                    app.board[newNodeRow][newNodeCol] = "Island"
                    addBridgeToBoard(app, node, newNode)
                    numBridges = random.randint(1,2)
                    app.islands[node] += [newNode]*numBridges
        for island in set(app.islands[node]):
            numBridges = app.islands[node].count(island)
            if island not in app.islands:
                app.islands[island] = [node]*numBridges
                generateBoardFromNode(app, island, depth + 1)
            elif node not in app.islands[island]:
                app.islands[island] += [node]*numBridges

def getPossibleNewNodePositions(app, node, dir):
    possiblePositions = []
    nodeRow = node[0]
    nodeCol = node[1]
    start = 0
    end = 0
    change = 0
    if dir == "UP" or dir == "DOWN":
        if dir == "UP":
            start = nodeRow - 2
            end = -1
            change = -1
        else:
            start = nodeRow + 2
            end = app.boardSize
            change = 1
        if (nodeRow+change > 6 or nodeRow+change < 0 or 
                        app.board[nodeRow+change][nodeCol] == "Bridge" or 
                        app.board[nodeRow+change][nodeCol] == "Island"):
            return []
        else:
            for row in range(start, end, change):
                if app.board[row][nodeCol] == None:
                    possiblePositions += [(row, nodeCol)]
                elif app.board[row][nodeCol] == "Bridge":
                    break
                elif app.board[row][nodeCol] == "Island":
                    if possiblePositions != []:
                        possiblePositions.pop()
                        possiblePositions += [(row, nodeCol)]
                    break
    elif dir == "LEFT" or dir == "RIGHT":
        if dir == "LEFT":
            start = nodeCol - 2
            end = -1
            change = -1
        else:
            start = nodeCol + 2
            end = app.boardSize
            change = 1
        if (nodeCol+change > 6 or nodeCol+change < 0 or 
                        app.board[nodeRow][nodeCol+change] == "Bridge" or 
                        app.board[nodeRow][nodeCol+change] == "Island"):
            return []
        else:
            for col in range(start, end, change):
                if app.board[nodeRow][col] == None:
                    possiblePositions += [(nodeRow, col)]
                elif app.board[nodeRow][col] == "Bridge":
                    break
                elif app.board[nodeRow][col] == "Island":
                    if possiblePositions != []:
                        possiblePositions.pop()
                        possiblePositions += [(nodeRow, col)]
                    break
    return possiblePositions

def addBridgeToBoard(app, node1, node2):
    if node1[0] == node2[0]:
        row = node1[0]
        if node1[1] > node2[1]:
            for col in range(node2[1] + 1, node1[1]):
                app.board[row][col] = "Bridge"
        else:
            for col in range(node1[1] + 1, node2[1]):
                app.board[row][col] = "Bridge"
    else:
        col = node1[1]
        if node1[0] > node2[0]:
            for row in range(node2[0] + 1, node1[0]):
                app.board[row][col] = "Bridge"
        else:
            for row in range(node1[0] + 1, node2[0]):
                app.board[row][col] = "Bridge"

def generateBlankBoard(app):
    for island in app.islands:
        app.currentIslands[island] = []
        app.currentBoard[island[0]][island[1]] = "Island"

def resetBoard(app):
    app.currentIslands = dict()
    app.currentBoard = [ ([None] * app.boardSize) for row in range(app.boardSize)]
    generateBlankBoard(app)

################################################################################
# Drawing Board
################################################################################

def drawIslands(app, canvas):
    adjacentNodes = []
    if app.firstIslandPressed != None:
        adjacentNodes = getAdjacentNodes(app, app.firstIslandPressed)
    for island in app.currentIslands:
        fill = None
        if island in adjacentNodes:
            fill = 'Yellow'
        drawIsland(app, canvas, island, fill)

def drawIsland(app, canvas, island, fill):
    cx, cy = getCellCenter(app, island[0], island[1])
    r = app.cellSize//2
    numBridges = len(app.islands[island])
    outline = "Black"
    if numBridges == len(app.currentIslands[island]): #island has correct number of bridges
        outline = "Green"
    elif numBridges < len(app.currentIslands[island]): #island has too many bridges
        outline = "Red"
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, width= 4, fill= fill, outline= outline)
    canvas.create_text(cx, cy, text= str(numBridges), font = "Ariel 15 bold", fill= outline)

def drawBridges(app, canvas):
    for island1 in app.currentIslands:
        for island2 in set(app.currentIslands[island1]):
            if app.currentIslands[island1].count(island2) == 2:
                drawDoubleBridge(app, canvas, island1, island2)
            else:
                drawSingleBridge(app, canvas, island1, island2)

def drawSingleBridge(app, canvas, island1, island2):
    x1, y1, x2, y2 = getSingleBridgeEndpoints(app, island1, island2)
    canvas.create_line(x1, y1, x2, y2, width= 4)

def drawDoubleBridge(app, canvas, island1, island2):
    x1, y1, x2, y2, x3, y3, x4, y4 = getDoubleBridgeEndpoints(app, island1, island2)
    canvas.create_line(x1, y1, x2, y2, width= 4)
    canvas.create_line(x3, y3, x4, y4, width= 4)

def getSingleBridgeEndpoints(app, island1, island2):
    cx1, cy1 = getCellCenter(app, island1[0], island1[1])
    cx2, cy2 = getCellCenter(app, island2[0], island2[1])
    if island1[0] == island2[0]: #same row
        y1 = cy1
        y2 = cy2
        if island1[1] < island2[1]:
            x1 = cx1 + app.cellSize//2
            x2 = cx2 - app.cellSize//2
            return x1, y1, x2, y2
        else:
            x1 = cx1 -app.cellSize//2
            x2 = cx2 + app.cellSize//2
            return x1, y1, x2, y2
    else: #same col
        x1 = cx1
        x2 = cx2
        if island1[0] < island2[0]:
            y1 = cy1 + app.cellSize//2
            y2 = cy2 - app.cellSize//2
            return x1, y1, x2, y2
        else:
            y1 = cy1 - app.cellSize//2
            y2 = cy2 + app.cellSize//2
            return x1, y1, x2, y2

def getDoubleBridgeEndpoints(app, island1, island2):
    cx1, cy1 = getCellCenter(app, island1[0], island1[1])
    cx2, cy2 = getCellCenter(app, island2[0], island2[1])
    if island1[0] == island2[0]: #same row
        y1 = cy1 + 5
        y2 = cy2 + 5
        y3 = cy1 - 5
        y4 = cy2 - 5
        if island1[1] < island2[1]:
            x1 = cx1 + app.cellSize//2
            x2 = cx2 - app.cellSize//2
            x3 = cx1 + app.cellSize//2
            x4 = cx2 - app.cellSize//2
            return x1, y1, x2, y2, x3, y3, x4, y4
        else:
            x1 = cx1 - app.cellSize//2
            x2 = cx2 + app.cellSize//2
            x3 = cx1 - app.cellSize//2
            x4 = cx2 + app.cellSize//2
            return x1, y1, x2, y2, x3, y3, x4, y4
    else: #same col
        x1 = cx1 + 5
        x2 = cx2 + 5
        x3 = cx1 - 5
        x4 = cx2 - 5
        if island1[0] < island2[0]:
            y1 = cy1 + app.cellSize//2
            y2 = cy2 - app.cellSize//2
            y3 = cy1 + app.cellSize//2
            y4 = cy2 - app.cellSize//2
            return x1, y1, x2, y2, x3, y3, x4, y4
        else:
            y1 = cy1 - app.cellSize//2
            y2 = cy2 + app.cellSize//2
            y3 = cy1 - app.cellSize//2
            y4 = cy2 + app.cellSize//2
            return x1, y1, x2, y2, x3, y3, x4, y4

def drawBoard(app, canvas):
    #outline of board(400x400)
    canvas.create_rectangle(app.width//2 - 200, app.height//2 - 200, 
                        app.width//2 + 200, app.height//2 + 200, width= 4) 
    drawIslands(app, canvas)
    drawBridges(app, canvas)

def getCellCenter(app, row, col):
    cx = app.lrMargin + app.cellSize*col + app.cellSize//2
    cy = app.udMargin + app.cellSize*row + app.cellSize//2
    return (cx, cy)

# from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
def getCell(app, x, y):
    col = int((x - app.lrMargin) / app.cellSize)
    row = int((y - app.udMargin) / app.cellSize)
    return (row, col)

def redrawAll(app, canvas):
    if app.startScreen:
        drawStartScreen(app, canvas)
    elif app.randomBoardScreen:
        drawRandomBoardScreen(app, canvas)
    elif app.practice1Screen:
        drawPractice1Screen(app, canvas)
    elif app.practice2Screen:
        drawPractice2Screen(app, canvas)
    elif app.practice3Screen:
        drawPractice3Screen(app, canvas)
    elif app.instructionsScreen:
        drawInstructionsScreen(app, canvas)
    elif app.helpScreen:
        drawHelpScreen(app, canvas)

runApp(width= 800, height= 600)
