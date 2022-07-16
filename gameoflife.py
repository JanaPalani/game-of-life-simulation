# importing the packages needed
import pygame
import time
import random
import copy

# initialising pygame
pygame.init()

# setting the dispaly 
display=pygame.display.set_mode((500,500))


dictionary={}
dictionary_copy={}
run = True
count = 0
neighbour_value = 0
state = 'notready'

clock = pygame.time.Clock()

while run:
    # filling the background colour 
    display.fill((0,0,0)) 

    for event in pygame.event.get():
        # to close the window opened 
        if event.type ==pygame.QUIT: 
            run = False

        if event.type == pygame.KEYDOWN:
            #  filling the population on a random 
            if event.key == pygame.K_SPACE:
                for i in range(100):
                    for j in range(100):
                        if i == 0 or j == 0 or i==99 or j ==99:
                            value = 0
                            dictionary[(i,j)] = value
                        else:
                            value = 1 if random.random() > 0.70 else 0
                            dictionary[(i, j)] = value

            #  settign the state variable to start the migaration of generation 
            if event.key == pygame.K_g:
                state = 'ready'
                
    # proliferation of the generation after pressing the key 'g'
    if state == 'ready':
        #  taking a copy of the dictionary 
        dictionary_copy = copy.deepcopy(dictionary)

        for i in range(1,99):
            for j in range(1,99):
                neighbour_value = dictionary[(i-1,j-1)]+dictionary[(i-1,j)]+dictionary[(i-1,j+1)]+dictionary[(i,j-1)]+dictionary[(i,j+1)]+dictionary[(i+1,j-1)]+dictionary[(i+1,j)]+dictionary[(i+1,j+1)]
                # checking the live plot
                if dictionary[(i,j)] == 1:
                    if neighbour_value <2 or neighbour_value>3:
                        dictionary_copy[(i,j)] = 0 
                #  checking the empty plot 
                elif dictionary[(i,j)] == 0:
                    if neighbour_value == 3:
                        dictionary_copy[(i,j)] = 1 
        # after checking all the cells or boxes reassigning the dictionary copy to dictionary
        dictionary = copy.deepcopy(dictionary_copy)
        time.sleep(0.1)

    #  create grids on the window
    for y in range(100):
        for x in range(100):
            pygame.draw.rect(display,(0,150,150),(x*5,y*5,5,5),1)



    # colouring the plots with the help of the dictionary that is uased for the checking purpose 
    for key, v in dictionary.items():
        x = key[0]
        y = key[1]
        pygame.draw.rect(display, (0, v * 150, v * 150), (x * 5, y * 5, 5, 5))
    pygame.display.update()

