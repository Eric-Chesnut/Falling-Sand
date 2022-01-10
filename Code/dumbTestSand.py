import sys, pygame, random

pygame.init()

height = 500
width = 500
board = [0] * (width + width*height + 1) #create array, fills it with 0's from board[0] to board[width + width*height] and a buffer cuz i can
tempBoard = [0] * (width + width*height + 1)

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
# array is 1d, but represents a 2d array, x = 6 y = 0 is board[6], x=6 y=1 is board[506], and so on

# set value at x, y 
def setBoard(x, y, val):
    board[x + y*width] = val

# get value at x, y
def getBoard(x, y):
    return board[x + y*width]

def setTempBoard(x, y, val):
    tempBoard[x + y*width] = val

def getTempBoard(x, y):
    return tempBoard[x + y*width]

# creates a ring of -1 around the array
def setBoarder():
    for y in range(height-1,-1,-1):
        setBoard(0, y, -1)
        setBoard(1, y, -1)
        setBoard(width, y, -1)
        setBoard(width-1, y, -1)
    for x in range(0,width):
        setBoard(x, 0, -1)
        setBoard(x, 1, -1)
        setBoard(x, height, -1)
        setBoard(x, height-1, -1)
       
def setTempBoarder():
    for y in range(height-1,-1,-1):
        setTempBoard(0, y, -1)
        setTempBoard(1, y, -1)
        setTempBoard(width, y, -1)
        setTempBoard(width-1, y, -1)
    for x in range(0,width):
        setTempBoard(x, 0, -1)
        setTempBoard(x, 1, -1)
        setTempBoard(x, height, -1)
        setTempBoard(x, height-1, -1)

def emptyTempBoard():
    tempBoard = [0] * (width + width*height + 1)
    setTempBoarder()

def copyBoard():
    for x in range(len(board)):
        board[x] = tempBoard[x]


def runSimTwo():
    direction = 1
    swaps = 0
    for y in range(height-2,1,-1):
        for x in range(2,width-2):
            if getBoard(x,y) == 1: # if it's sand
                if getBoard(x,y+1) == 0 or getBoard(x,y+1) == 2: # if spot below sand is empty or has watter
                    if getTempBoard(x, y+1) == 0 or getTempBoard(x, y+1) == 2: # make sure the spot is still empty or water
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,1)
                    elif getTempBoard(x-direction,y+1) == 0 or getTempBoard(x-direction,y+1) == 2: # spot down to the first side
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x+direction,y+1) == 0 or getTempBoard(x+direction,y+1) == 2: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,1)
                elif getBoard(x-direction,y+1) == 0 or getBoard(x-direction,y+1) == 2: # spot down to the first side 
                    if getTempBoard(x-direction,y+1) == 0 or getTempBoard(x-direction,y+1) == 2: # still empty/water?
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x, y+1) == 0 or getTempBoard(x, y+1) == 2: # check if center is water/empty now
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x+direction,y+1) == 0 or getTempBoard(x+direction,y+1) == 2: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,1)
                elif getBoard(x+direction,y+1) == 0 or getBoard(x+direction,y+1) == 2: # spot down to the second side
                    if getTempBoard(x+direction,y+1) == 0 or getTempBoard(x+direction,y+1) == 2: # still empty/water?
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x, y+1) == 0 or getTempBoard(x, y+1) == 2: # check if center is water/empty now
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x-direction,y+1) == 0 or getTempBoard(x-direction,y+1) == 2: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,1)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,1)
                else:
                    setTempBoard(x,y,1) # sand not moving
            elif getBoard(x,y) == 2: # if it's water
                if getBoard(x,y+1) == 0: # if spot below water is empty 
                    if getTempBoard(x, y+1) == 0: # make sure the spot is still empty
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,2)
                    elif getTempBoard(x-direction,y+1) == 0: # spot down to the first side
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x+direction,y+1) == 0: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,2)
                elif getBoard(x-direction,y+1) == 0: # spot down to the first side 
                    if getTempBoard(x-direction,y+1) == 0: # still empty?
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x, y+1) == 0: # check if center is empty now
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x+direction,y+1) == 0: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,2)
                elif getBoard(x+direction,y+1) == 0: # spot down to the second side
                    if getTempBoard(x+direction,y+1) == 0: # still empty?
                        setTempBoard(x,y,getTempBoard(x+direction,y+1))
                        setTempBoard(x+direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x, y+1) == 0: # check if center is empty now
                        setTempBoard(x,y,getTempBoard(x,y+1))
                        setTempBoard(x,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    elif getTempBoard(x-direction,y+1) == 0: # spot down to the second side
                        setTempBoard(x,y,getTempBoard(x-direction,y+1))
                        setTempBoard(x-direction,y+1,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,2)
                elif getBoard(x+direction,y) == 0: # spot next to it is empty
                    if getTempBoard(x+direction,y) == 0: # still empty?
                        setTempBoard(x,y,getTempBoard(x+direction,y))
                        setTempBoard(x+direction,y,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,2)
                elif getBoard(x-direction,y) == 0: # other side is empty
                    if getTempBoard(x-direction,y) == 0: # still empty?
                        setTempBoard(x,y,getTempBoard(x-direction,y))
                        setTempBoard(x-direction,y,2)
                        swaps = random.randint(0,1)
                        if swaps == 0:
                            direction = 1
                        else:
                            direction = -1
                    else:
                        setTempBoard(x,y,2)
                else:
                    setTempBoard(x,y,2) # water didn't move
    copyBoard()
    emptyTempBoard()
# makes sand fall
# currently water (2) can move right until it hits something, but just one square left
# things on the far left, so x = 0, move twice as fast as other objects, and it will cause a crash
# if an thing is at (0,0) and (1,0), if an object is at (0,1) it will check position (0,0), find it's full,
# it will then either check position (1,0), which it will also find full, or/after checking (1,0), it will
# attempt to check position (-1,0), this doesn't exist in the array and will cause a crash, same should happen on the right side
# objects at (500, x) don't move at double speed, still causes a crash, tries to access (501, 0)
# doesn't crash anymore.... why? it does pile up on the other side of the screen though, i get why this is happening
# at (0, y) it checks (1, y-1) and (-1, y-1), (-1, y-1) happens to be the same as (500, y-1-1), so it can move to that space
# works the other way too, (500, y), (499, y-1), (501, y-1) = (0, y)
# why not put a border, (0, 0-y), (0-500, y), (500, y-0), and (500-0, 0), it will never have to check the end spaces and won't run into this issue
# i was thinking a border would make it look nicer anyway, especially seing as anything at y = 0 isn't really visible
# the right bias would still exist
# one problem at a time, fix the teleporting objects
# border fixes the piling on the other side of the screen issue
# water will pool on the left, it's because the algorithm goes from left to right, it's hard for a group of water to move right, easy to move left
def runSimulation():
    direction = 1
    swaps = 0
    for y in range(height-2,1,-1):
        for x in range(2,width-2):
            if getBoard(x,y) == 1: # if it's sand
                if getBoard(x,y+1) == 0 or getBoard(x,y+1) == 2: # if spot below sand is empty or has watter
                    setBoard(x,y,getBoard(x,y+1))
                    setBoard(x,y+1,1)
                elif getBoard(x-direction,y+1) == 0 or getBoard(x-direction,y+1) == 2: # spot down to the first side 
                    setBoard(x,y,getBoard(x-direction,y+1))
                    setBoard(x-direction,y+1,1)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1
                elif getBoard(x+direction,y+1) == 0 or getBoard(x+direction,y+1) == 2: # spot down to the second side
                    setBoard(x,y,getBoard(x+direction,y+1))
                    setBoard(x+direction,y+1,1)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1
            elif getBoard(x,y) == 2: # if it's water
                if getBoard(x,y+1) == 0: # if spot below water is empty 
                    setBoard(x,y,0)
                    setBoard(x,y+1,2)
                elif getBoard(x-direction,y+1) == 0: # spot down to the first side 
                    setBoard(x,y,0)
                    setBoard(x-direction,y+1,2)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1
                elif getBoard(x+direction,y+1) == 0: # spot down to the second side
                    setBoard(x,y,0)
                    setBoard(x+direction,y+1,2)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1
                elif getBoard(x+direction,y) == 0: # spot next to it is empty
                    setBoard(x,y,0)
                    setBoard(x+direction,y,2)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1
                elif getBoard(x-direction,y) == 0: # other side is empty
                    setBoard(x,y,0)
                    setBoard(x-direction,y,2)
                    swaps = random.randint(0,1)
                    if swaps == 0:
                        direction = 1
                    else:
                        direction = -1

def addSand(x,y):
    setBoard(x,y,1)

def addWater(x,y):
    setBoard(x,y,2)
    
def drawBoard():
    screen.fill((255, 255, 255)) # Fill the screen with white
    for y in range(0,height):
        for x in range(0,width):
            if getBoard(x,y) == 1: #sand
                pygame.draw.rect(screen, (194, 178, 128), (x, y, 1, 1)) # color, (x position, y position, width, height) rectangle specs
            elif getBoard(x,y) == 2: #water
                pygame.draw.rect(screen, (0, 0, 255), (x, y, 1, 1))
            elif getBoard(x,y) == -1: #border
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 1, 1))
    # Flip the display
    pygame.display.flip()


def playGame():
    running = True
    swap = 0
    while running:
        clock.tick(60)
        # Did the user click the window close button?
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if quit is selected
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # if mouse input has been pressed down (right, left, middle, all mouse buttons)
                x, y = event.pos
                if(getBoard(x,y) == 0): #check that the spot is empty
                    if event.button == 3:
                        addWater(x,y)
                    else:
                        addSand(x,y)
        # end of event loop
        runSimTwo()
        
        if swap == 1:
            addSand(250,3)
            #addSand(255,0)
            #addSand(220,0)
            #addSand(240,0)
            swap = 0
        else:
            swap = 1
        drawBoard()
                
#for x in board:
#   print(x)

def main():
    setBoarder()
    emptyTempBoard()
    #print (tempBoard[0])
    playGame()
    # Done! Time to quit.
    pygame.quit()

main()