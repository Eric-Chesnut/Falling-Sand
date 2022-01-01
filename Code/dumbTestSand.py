import sys, pygame, random

pygame.init()

height = 500
width = 500
board = [0] * (width + width*height + 1) #create array, fills it with 0's from board[0] to board[width + width*height] and a buffer cuz i can
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
# array is 1d, but represents a 2d array, x = 6 y = 0 is board[6], x=6 y=1 is board[506], and so on

# set value at x, y 
def setBoard(x, y, val):
    board[x + y*width] = val

# get value at x, y
def getBoard(x, y):
    return board[x + y*width]

# makes sand fall
def runSimulation():
    direction = 1
    swaps = 0
    for y in range(height-1,-1,-1):
        for x in range(0,width+1):
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
    for y in range(0,height+1):
        for x in range(0,width+1):
            if getBoard(x,y) == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 1, 1)) # color, (x position, y position, width, height) rectangle specs
            elif getBoard(x,y) == 2:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, 1, 1))
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
                if event.button == 3:
                    addWater(x,y)
                else:
                    addSand(x,y)
        # end of event loop
        runSimulation()
        if swap == 1:
            addSand(250,0)
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
    playGame()
    # Done! Time to quit.
    pygame.quit()

main()