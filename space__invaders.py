import pygame
import random
import csv

pygame.init()

leaderboard = False
instructions = False
menu_exit = False
game_exit = False
paused = False
game_loop = False
game_over = False
export_data = False
difficulty_selection = False
a = [0] * 48
alien = [0] * 48
alien_x = 50
alien_y = 60
alien_const_z = 0
alien_const_y = 0
speed_of_ship = 0
ship_x = 350
ship_y = 400
player_laser_x = 0
player_laser_y = 375
player_const_a = 0
player_const_b = 0
score = 0
collision_alien = False
collision_player_count = 0
collision_player = False
collide = False
name = str()
roundnum = 1
name_entered = False
entering_name = False
freeze_screen = False

gameDisplay = pygame.display.set_mode((700,500),pygame.RESIZABLE)
pygame.display.set_caption('Space Invaders')
game_bg = pygame.image.load("game-bg.jpg")
game_bg = pygame.transform.scale(game_bg,(700,500))
gameover_bg = pygame.image.load("game-over-bg.jpg")
gameover_bg = pygame.transform.scale(gameover_bg,(700,500))
menu_bg = pygame.image.load("main-menu-bg.jpg")
menu_bg = pygame.transform.scale(menu_bg,(700,500))
mode_select_bg = pygame.image.load("mode-select-bg.jpg")
mode_select_bg = pygame.transform.scale(mode_select_bg,(700,500))
paused_bg = pygame.image.load("paused-bg.jpg")
paused_bg = pygame.transform.scale(paused_bg,(700,500))
leaderboard_bg = pygame.image.load("leaderboard_bg.jpg")
leaderboard_bg = pygame.transform.scale(leaderboard_bg,(700,500))
instructions_bg = pygame.image.load("instructions-bg.jpg")
instructions_bg = pygame.transform.scale(instructions_bg,(700,500))

"""Creates a class for the aliens, with 4 methods. The method spawn displays an
alien on the UI, while the method delete deletes an alien. The method find_x and
find_y are used to return the x and y coordinate of an alien"""
class aliens():
    def __init__(self,img,pos_x,pos_y):
        self.img = img
        self.pos_x = pos_x
        self.pos_y = pos_y
    def spawn(self):
        alien_img = pygame.image.load(self.img)
        gameDisplay.blit(alien_img,(self.pos_x,self.pos_y))
    def delete(self):
        alien_img = pygame.image.load(self.img)
        del alien_img
    def find_x(self):
        return self.pos_x
    def find_y(self):
        return self.pos_y

"""Creates a class for the spaceship, with 2 methods. The method spawn displays
the spaceship on the UI, while the method delete deletes an alien."""
class player_spaceship():
    def __init__(self,img):
        self.img = img
    def spawn(self,pos_x,pos_y):
        spaceship_img = pygame.image.load(self.img)
        gameDisplay.blit(spaceship_img,(pos_x,pos_y))
    def delete(self,pos_x,pos_y):
        spaceship_img = pygame.image.load(self.img)
        del spaceship_img        


#This function renders the text passed into the fuction
def text_objects(text,font):
    textSurface = font.render(text, True,(225,225,225))
    return textSurface, textSurface.get_rect()

#This function displays a message to the user interface
def display_message(text,x,y,size):
    largeText = pygame.font.Font('C:\WINDOWS\Fonts\ARIALN.TTF',size)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)

"""This function checks to see if the player laser has hit an alien, if it has it returns the
local variable collide as true. Once collide has been returned, collide is then set to
false again"""
def collisions(collide):
    collide = False
    if player_laser_x >= alien_x and player_laser_x <= (alien_x + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[0] += 1
        if a[0] == 5: collide = True
    elif player_laser_x >= (alien_x + 50) and player_laser_x <= (alien_x + 50 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[1] += 1
        if a[1] == 5: collide = True
    elif player_laser_x >= (alien_x + 100) and player_laser_x <= (alien_x + 100 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[2] += 1
        if a[2] == 5: collide = True
    elif player_laser_x >= (alien_x + 150) and player_laser_x <= (alien_x + 150 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[3] += 1
        if a[3] == 5: collide = True
    elif player_laser_x >= (alien_x + 200) and player_laser_x <= (alien_x + 200 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[4] += a[4] + 1
        if a[4] == 5: collide = True
    elif player_laser_x >= (alien_x + 250) and player_laser_x <= (alien_x + 250 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[5] += 1
        if a[5] == 5: collide = True
    elif player_laser_x >= (alien_x + 300) and player_laser_x <= (alien_x + 300 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[6] += 1
        if a[6] == 5: collide = True
    elif player_laser_x >= (alien_x + 350) and player_laser_x <= (alien_x + 350 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[7] += 1
        if a[7] == 5: collide = True
    elif player_laser_x >= (alien_x + 400) and player_laser_x <= (alien_x + 400 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[8] += 1
        if a[8] == 5: collide = True
    elif player_laser_x >= (alien_x + 450) and player_laser_x <= (alien_x + 450 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[9] += 1
        if a[9] == 5: collide = True
    elif player_laser_x >= (alien_x + 500) and player_laser_x <= (alien_x + 500 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[10] += 1
        if a[10] == 5: collide = True
    elif player_laser_x >= (alien_x + 550) and player_laser_x <= (alien_x + 550 + 30) and player_laser_y >= alien_y and player_laser_y <= (alien_y + 30):
        a[11] += 1
        if a[11] == 5: collide = True
                
    if player_laser_x >= alien_x and player_laser_x <= (alien_x + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[12] += 1
        if a[12] == 5: collide = True
    elif player_laser_x >= (alien_x + 50) and player_laser_x <= (alien_x + 50 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[13] += 1
        if a[13] == 5: collide = True
    elif player_laser_x >= (alien_x + 100) and player_laser_x <= (alien_x + 100 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[14] += 1
        if a[14] == 5: collide = True
    elif player_laser_x >= (alien_x + 150) and player_laser_x <= (alien_x + 150 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[15] += 1
        if a[15] == 5: collide = True
    elif player_laser_x >= (alien_x + 200) and player_laser_x <= (alien_x + 200 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[16] += 1
        if a[16] == 5: collide = True
    elif player_laser_x >= (alien_x + 250) and player_laser_x <= (alien_x + 250 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[17] += 1
        if a[17] == 5: collide = True
    elif player_laser_x >= (alien_x + 300) and player_laser_x <= (alien_x + 300 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[18] += 1
        if a[18] == 5: collide = True
    elif player_laser_x >= (alien_x + 350) and player_laser_x <= (alien_x + 350 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[19] += 1
        if a[19] == 5: collide = True
    elif player_laser_x >= (alien_x + 400) and player_laser_x <= (alien_x + 400 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[20] += 1
        if a[20] == 5: collide = True
    elif player_laser_x >= (alien_x + 450) and player_laser_x <= (alien_x + 450 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[21] += 1
        if a[21] == 5: collide = True
    elif player_laser_x >= (alien_x + 500) and player_laser_x <= (alien_x + 500 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[22] += 1
        if a[22] == 5: collide = True
    elif player_laser_x >= (alien_x + 550) and player_laser_x <= (alien_x + 550 + 30) and player_laser_y >= (alien_y + 40) and player_laser_y <= (alien_y + 30 + 40):
        a[23] += 1
        if a[23] == 5: collide = True

    if player_laser_x >= alien_x and player_laser_x <= (alien_x + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[24] += 1
        if a[24] == 5: collide = True
    elif player_laser_x >= (alien_x + 50) and player_laser_x <= (alien_x + 50 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[25] += 1
        if a[25] == 5: collide = True
    elif player_laser_x >= (alien_x + 100) and player_laser_x <= (alien_x + 100 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[26] += 1
        if a[26] == 5: collide = True
    elif player_laser_x >= (alien_x + 150) and player_laser_x <= (alien_x + 150 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[27] += 1
        if a[27] == 5: collide = True
    elif player_laser_x >= (alien_x + 200) and player_laser_x <= (alien_x + 200 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[28] += 1
        if a[28] == 5: collide = True
    elif player_laser_x >= (alien_x + 250) and player_laser_x <= (alien_x + 250 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[29] += 1
        if a[29] == 5: collide = True
    elif player_laser_x >= (alien_x + 300) and player_laser_x <= (alien_x + 300 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[30] += 1
        if a[30] == 5: collide = True
    elif player_laser_x >= (alien_x + 350) and player_laser_x <= (alien_x + 350 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[31] += 1
        if a[31] == 5: collide = True
    elif player_laser_x >= (alien_x + 400) and player_laser_x <= (alien_x + 400 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[32] += 1
        if a[32] == 5: collide = True
    elif player_laser_x >= (alien_x + 450) and player_laser_x <= (alien_x + 450 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[33] += 1
        if a[33] == 5: collide = True
    elif player_laser_x >= (alien_x + 500) and player_laser_x <= (alien_x + 500 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[34] += 1
        if a[34] == 5: collide = True
    elif player_laser_x >= (alien_x + 550) and player_laser_x <= (alien_x + 550 + 30) and player_laser_y >= (alien_y + 80) and player_laser_y <= (alien_y + 30 + 80):
        a[35] += 1
        if a[35] == 5: collide = True
            
    if player_laser_x >= alien_x and player_laser_x <= (alien_x + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[36] += 1
        if a[36] == 5: collide = True
    elif player_laser_x >= (alien_x + 50) and player_laser_x <= (alien_x + 50 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[37] += 1
        if a[37] == 5: collide = True
    elif player_laser_x >= (alien_x + 100) and player_laser_x <= (alien_x + 100 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[38] += 1
        if a[38] == 5: collide = True 
    elif player_laser_x >= (alien_x + 150) and player_laser_x <= (alien_x + 150 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[39] += 1
        if a[39] == 5: collide = True 
    elif player_laser_x >= (alien_x + 200) and player_laser_x <= (alien_x + 200 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[40] += 1
        if a[40] == 5: collide = True 
    elif player_laser_x >= (alien_x + 250) and player_laser_x <= (alien_x + 250 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[41] += 1
        if a[41] == 5: collide = True 
    elif player_laser_x >= (alien_x + 300) and player_laser_x <= (alien_x + 300 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[42] = a[42] + 1
        if a[42] == 5: collide = True 
    elif player_laser_x >= (alien_x + 350) and player_laser_x <= (alien_x + 350 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[43] += 1
        if a[43] == 5: collide = True 
    elif player_laser_x >= (alien_x + 400) and player_laser_x <= (alien_x + 400 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[44] += 1
        if a[44] == 5: collide = True
    elif player_laser_x >= (alien_x + 450) and player_laser_x <= (alien_x + 450 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[45] += 1
        if a[45] == 5: collide = True
    elif player_laser_x >= (alien_x + 500) and player_laser_x <= (alien_x + 500 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[46] += 1
        if a[46] == 5: collide = True
    elif player_laser_x >= (alien_x + 550) and player_laser_x <= (alien_x + 550 + 30) and player_laser_y >= (alien_y + 120) and player_laser_y <= (alien_y + 30 + 120):
        a[47] += 1
        if a[47] == 5: collide = True
    return collide

"""This function spawns all the 48 aliens. Then it checks if any of the aliens have
been hit, if they have this function deletes the aliens hit from the UI, if they haven't then this function displays the aliens on the UI"""
def spawn_multiple_aliens(img,x,y,counter_start,counter_end):
    collisions(collision_alien)
    for counter in range(counter_start,counter_end):
        alien[counter] = aliens(img,x,y)
        if a[counter] < 5:
            alien[counter].spawn()
            x += 50
        elif a[counter] >= 5:
            alien[counter].delete()
            x += 50

#The game loop runs while the game window is open
while game_exit == False:
    
    #This loop runs while the user is on the main menu
    while menu_exit == False:
        #Display the background for the main menu
        gameDisplay.blit(menu_bg,(0,0))
        #Gather all the events occuring in the user interface
        for event in pygame.event.get():
            #If the user clickes on the close button of the window then do the following
            if event.type == pygame.QUIT:
                menu_exit = True
                game_exit = True
        #Stores the position of the cursor in the variable mouse
        mouse = pygame.mouse.get_pos()
        #Stores the status of the mouse buttons in the variable click
        click = pygame.mouse.get_pressed()
        #Displays the following messages on the user interface
        display_message('SPACE INVADERS',350,50,50)
        display_message('START GAME',350,385,20)
        display_message('INSTRUCTIONS',350,420,20)
        display_message('LEADERBOARD',350,455,20)
        #Checks if 'START GAME','INSTRUCTIONS' or 'LEADERBOARD' have been clicked, if they have the user is directed to the respective page
        if mouse[0] >= 297 and mouse[0] <= 402 and mouse[1] >= 378 and mouse[1] <= 391 and click[0] == 1: 
            menu_exit = True
            difficulty_selection = True
        elif mouse[0] >= 290 and mouse[0] <= 410 and mouse[1] >= 413 and mouse[1] <= 426 and click[0] == 1:
            menu_exit = True
            instructions = True
        elif mouse[0] >= 289 and mouse[0] <= 411 and mouse[1] >= 448 and mouse[1] <= 461 and click[0] == 1:
            menu_exit = True
            leaderboard = True
            #Updates the user interface
        pygame.display.update()

    #This loop runs while the user is on the difficulty selection page
    while difficulty_selection == True:
        gameDisplay.blit(mode_select_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                difficulty_selection = False
                game_exit = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Displays the following messages on the user interface
        display_message('SPACE INVADERS',350,50,50)
        display_message('PLEASE SELECT THE DIFFICULTY',350,130,25)
        display_message('EASY',350,235,20)
        display_message('MEDIUM',350,270,20)
        display_message('HARD',350,305,20)
        #Checks if "EASY", "MEDIUM" OR "HARD" have been clicked, if they have the user is directed to the game page; with the game configured to play the relevant mode
        if mouse[0] >= 329 and mouse[0] <= 371 and mouse[1] >= 228 and mouse[1] <= 241 and click[0] == 1:
            mode = "EASY"
            speed_per_round = 0.10
            speed_of_aliens = 0.20
            difficulty_selection = False
            game_loop = True
        elif mouse[0] >= 317 and mouse[0] <= 382 and mouse[1] >= 263 and mouse[1] <= 276 and click[0] == 1:
            mode = "MEDIUM"
            speed_per_round = 0.20
            speed_of_aliens = 0.30
            difficulty_selection = False
            game_loop = True    
        elif mouse[0] >= 328 and mouse[0] <= 372 and mouse[1] >= 298 and mouse[1] <= 311 and click[0] == 1:
            mode = "HARD"
            speed_per_round = 0.30
            speed_of_aliens = 0.40
            difficulty_selection = False
            game_loop = True
        pygame.display.update()

    #This loop runs while the user is on the game page
    while game_loop == True:
        gameDisplay.blit(game_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
                game_exit = True
            #If the user presses down on a key then do the following
            if event.type == pygame.KEYDOWN:
                #Allows the user to move their ship left to right
                if event.key == pygame.K_LEFT:
                    speed_of_ship = -5
                elif event.key == pygame.K_RIGHT:
                    speed_of_ship = 5
                #Shoots the player's laser if the space bar is pressed
                elif event.key == pygame.K_SPACE:
                    player_const_a = 1
                #Directs the user to the paused page if the "P" key is clicked
                elif event.key == pygame.K_p:
                    paused = True
                    game_loop = False
            #If the user releases a key then do the following
            if event.type == pygame.KEYUP:
                #If the user releases either the right or left key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    speed_of_ship = 0
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Spawns the aliens
        spawn_multiple_aliens('alien.png',alien_x,alien_y,0,12)
        spawn_multiple_aliens('alien-2.png',alien_x,(alien_y + 40),12,24)
        spawn_multiple_aliens('alien.png',alien_x,(alien_y + 80),24,36)
        spawn_multiple_aliens('alien-2.png',alien_x,(alien_y + 120),36,48)
        #Creates an objects from the class player_spaceship
        spaceship = player_spaceship('spaceship.png')
        life1 = player_spaceship('spaceship_lives.png')
        life2 = player_spaceship('spaceship_lives.png')
        life3 = player_spaceship('spaceship_lives.png')
        #Displays the object called spaceship on the UI
        spaceship.spawn(ship_x,ship_y)
        #Adjusts the x value of the ship
        ship_x += speed_of_ship
        #Sets the limit to which the aliens can drop down to, before ending the game
        drop_limit = alien_y + 152
        #Stops the spaceship from going of the screen
        if ship_x <= 15:
            ship_x = 15
        elif ship_x >= 650:
            ship_x = 650
        #Assigns the value being returned from the function collisions to the variable collision_check
        collision_check = collisions(collision_alien)

        #Manages the operation of the spaceship's laser
        if player_const_b == 0:
            player_laser_x = ship_x + 16
                        
        if player_const_a == 1:
            pygame.draw.line(gameDisplay,(225,225,225),(player_laser_x,(player_laser_y - 15)),(player_laser_x,(player_laser_y - 5)))
            player_laser_y = player_laser_y - 3
            player_const_b = 1
            
        #Allows the player to shoot their laser again when the laser has gone off the screen
        if player_laser_y <= -5:
            player_const_a = 0
            player_const_b = 0
        #Allows the player to shoot their laser again when the laser has hit an alien
        if collision_check == True:
            score += 50
            player_const_a = 0
            player_const_b = 0

        if player_const_a == 0:
            player_laser_y = 395

        #Selects which alien is going to shoot the laser and assigns the x and y coordinates of the laser
        if alien_const_y == 0:
            counter = random.randint(36,47)
            if a[counter] < 5:
                shoot_x = alien[counter].find_x()
                shoot_y = alien[counter].find_y()
            elif a[counter] >= 5:
                if a[(counter - 12)] < 5:
                    shoot_x = alien[(counter - 12)].find_x()
                    shoot_y = alien[(counter - 12)].find_y()
                elif a[(counter - 12)] >= 5:
                    if a[(counter - 24)] < 5:
                        shoot_x = alien[(counter - 24)].find_x()
                        shoot_y = alien[(counter - 24)].find_y()
                    elif a[(counter - 24)] >= 5:
                        if a[(counter - 36)] < 5:
                            shoot_x = alien[(counter - 36)].find_x()
                            shoot_y = alien[(counter - 36)].find_y()
                        elif a[(counter - 36)] >= 5:
                            alien_const_y = 0

        #Changes the drop limit of the aliens when required
        if a[36] >= 5 and a[37] >= 5 and a[38] >= 5 and a[39] >= 5 and a[40] >= 5 and a[41] >= 5 and a[42] >= 5 and a[43] >= 5 and a[44] >= 5 and a[45] >= 5 and a[46] >= 5 and a[47] >= 5:
            drop_limit -= 40
        if a[36] >= 5 and a[37] >= 5 and a[38] >= 5 and a[39] >= 5 and a[40] >= 5 and a[41] >= 5 and a[42] >= 5 and a[43] >= 5 and a[44] >= 5 and a[45] >= 5 and a[46] >= 5 and a[47] >= 5 and a[24] >= 5 and a[25] >= 5 and a[26] >= 5 and a[27] >= 5 and a[28] >= 5 and a[29] >= 5 and a[30] >= 5 and a[31] >= 5 and a[32] >= 5 and a[33] >= 5 and a[34] >= 5 and a[35] >= 5:
            drop_limit -= 40
        if a[12] >= 5 and a[13] >= 5 and a[14] >= 5 and a[15] >= 5 and a[16] >= 5 and a[17] >= 5 and a[18] >= 5 and a[19] >= 5 and a[20] >= 5 and a[21] >= 5 and a[22] >= 5 and a[23] >= 5:
            drop_limit -= 40

        #Displays a warning message when the aliens are close to the spaceship
        if (ship_y - 40) <= (drop_limit):
            display_message('WARNING - ALIENS APPROACHING',350,470,20)

        #Allows the aliens to move right to left without going off the screen
        alien_const_z = alien_const_z + 0.5
        if alien_const_z >= 0:
            alien_x -= speed_of_aliens
        elif alien_const_z <= 0:
            alien_x += speed_of_aliens

        if alien_x <= 15:
            alien_const_z = -200

        #Checks if the alien's laser has hit the spaceship,if it has then a life is taken off and the user is directed to the frozen screen
        if shoot_x >= (ship_x - 16) and shoot_x <= (ship_x + 16) and shoot_y >= 370 and shoot_y <= 392:
            collision_player_count += 1
            collision_player = True
            freeze_screen = True

        #Checks if the aliens have hit the right side of the screen, if they have they go down a step and start to move in the opposite direction              
        if alien_x  >= 95:
            alien_y += 10
            alien_const_z = 80
            
        if drop_limit >= 380:
            collision_player_count = 3
            freeze_screen = True

        #Manages the shooting of the alien's laser
        alien_const_y = 1 
        pygame.draw.line(gameDisplay,(225,225,225),((shoot_x + 15),(shoot_y + 40)),((shoot_x + 15),(shoot_y + 30)))
        shoot_y += 3

        #Checks if the alien's laser has hit the spaceship or if it has gone off the screen, if it has then the alien's laser is reset     
        if shoot_y > 515.5 or collision_player == True:
            alien_const_y = 0
            pygame.draw.rect(gameDisplay,(0,0,0),[shoot_x,shoot_y,50,50])

        #Provides the user real time information about their lives
        if collision_player_count == 0:
            life1.spawn(580,10)
            life2.spawn(620,10)
            life3.spawn(660,10)
            
        elif collision_player_count == 1:
            life1.delete(580,10)
            life2.spawn(620,10)  
            life3.spawn(660,10)
            
        elif collision_player_count == 2:
            life1.delete(580,10)
            life2.delete(620,10)
            life3.spawn(660,10)
            
        collision_player = False
        
        #Checks if all the aliens have been hit, if they have then the round number incrases by 1 and all the aliens are reset
        if a[0] >=5 and a[1] >=5 and a[2] >=5 and a[3] >=5 and a[4] >=5 and a[5] >=5 and a[6] >=5 and a[7] >=5 and a[8] >=5 and a[9] >=5 and a[10] >=5 and a[11] >=5 and a[12] >=5 and a[13] >=5 and a[14] >=5 and a[15] >=5 and a[16] >=5 and a[17] >=5 and a[18] >=5 and a[19] >=5 and a[20] >=5 and a[21] >=5 and a[22] >=5 and a[23] >=5 and a[24] >=5 and a[25] >=5 and a[26] >=5 and a[27] >=5 and a[28] >=5 and a[29] >=5 and a[30] >=5 and a[31] >=5 and a[32] >=5 and a[33] >=5 and a[34] >=5 and a[35] >=5 and a[36] >=5 and a[37] >=5 and a[38] >=5 and a[39] >=5 and a[40] >=5 and a[41] >=5 and a[42] >=5 and a[43] >=5 and a[44] >=5 and a[45] >=5 and a[46] >=5 and a[47] >=5:
            for counter in range(0,48):
                a[counter] = 0
            alien_x = 50
            alien_y = 85
            roundnum += 1
            speed_of_aliens = speed_of_aliens + speed_per_round
            
        #Displays the following items to the user interface
        display_message('Score',30,25,20)
        display_message('Lives',540,25,20)
        display_message(str(score),85,25,20)
        display_message('Round',150,25,20)
        display_message(str(roundnum),190,25,20)

        #Displays the pause icon
        pause_icon = pygame.image.load('pause-sign.png')
        pause_icon = pygame.transform.scale(pause_icon,(10,15))
        gameDisplay.blit(pause_icon,(500,18))
    
        #Checks if the pause icon has been hit, if it has the user is directed to the paused page
        if mouse[0] >= 502 and mouse[0] <= 508 and mouse[1] >= 18 and mouse[1] <= 32 and click[0] == 1:
            paused = True
            game_loop = False

        #This loop runs when the user has lost a life
        while freeze_screen == True:
            gameDisplay.blit(game_bg,(0,0))
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   #Checks if the space bar has been clicked, it it has then the user's screen unfreezes and is able to play again
                   if event.key == pygame.K_SPACE:
                       freeze_screen = False
            #Spawns the spaceship in the centre and displays the message 'PRESS SPACE TO CONTINUE' whenever the player loses a life, and when all their lives are finished the game over message is displayed
            player_const_a = 0
            player_const_b = 0
            speed_of_ship = 0
            ship_x = 350
            if collision_player_count == 0:
                life1.spawn(580,10)
                life2.spawn(620,10)
                life3.spawn(660,10)
                display_message('PRESS SPACE TO CONTINUE',365,470,20)
            elif collision_player_count == 1:
                life1.delete(580,10)
                life2.spawn(620,10)  
                life3.spawn(660,10)
                display_message('PRESS SPACE TO CONTINUE',365,470,20)
            elif collision_player_count == 2:
                life1.delete(580,10)
                life2.delete(620,10)
                life3.spawn(660,10)
                display_message('PRESS SPACE TO CONTINUE',365,470,20)
            elif collision_player_count == 3:
                display_message('GAME OVER - PRESS SPACE TO CONTINUE',350,470,20)
                game_loop = False
                game_over = True
            spaceship.spawn(350,400)
            #Updates only certain parts of the user interface
            pygame.display.update([160,460,380,20])
            pygame.display.update([580,0,240,50])
            pygame.display.update([0,380,700,60])
        pygame.display.update()

    #This loop runs while the user is on the paused page
    while paused == True:
        gameDisplay.blit(paused_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                game_exit = True
            #Checks if the 'P' key has been pressed, if it has then the user is directed back to the game page
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    game_loop = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Displays the following messages to the user interface
        display_message('SPACE INVADERS',350,50,50)
        display_message('PAUSED',350,100,30)
        display_message('RESUME',350,370,20)
        display_message('RESTART',350,405,20)
        display_message('MAIN MENU',350,440,20)
        
        #Checks if 'RESUME','RESTART' or 'MAIN MENU' have been clicked, if they have the user is directed to the respective page; with all the previous game's data deleted
        if mouse[0] >= 315 and mouse[0] <= 384 and mouse[1] >= 363 and mouse[1] <= 376 and click[0] == 1:
            paused = False
            game_loop = True
        elif mouse[0] >= 313 and mouse[0] <= 386 and mouse[1] >= 398 and mouse[1] <= 411 and click[0] == 1:
            score = 0
            collision_player_count = 0
            alien_const_y = 0
            alien_y = 85
            alien_x = 50
            ship_x = 350
            roundnum = 1
            for counter in range(0,48):
                a[counter] = 0
            paused = False
            difficulty_selection = True
        elif mouse[0] >= 303 and mouse[0] <= 397 and mouse[1] >= 433 and mouse[1] <= 446 and click[0] == 1:
            score = 0
            collision_player_count = 0
            alien_const_y = 0
            alien_y = 85
            alien_x = 50
            ship_x = 350
            roundnum = 1
            for counter in range(0,48):
                a[counter] = 0
            paused = False
            menu_exit = False
        pygame.display.update()

    #This loop runs while the user is on the game over page    
    while game_over == True:
        gameDisplay.blit(gameover_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        game_over = False
                        game_exit = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Display the following messages to the user interface
        display_message('SPACE INVADERS',350,50,50)
        display_message('GAME OVER',350,100,30)
        display_message('Name',255,200,19)
        display_message('Score',260,240,19)
        display_message('Mode',255,280,19)
        pygame.draw.rect(gameDisplay,(4,12,25),[300,190,100,21])
        pygame.draw.rect(gameDisplay,(4,12,25),[402,190,30,21])
        pygame.draw.rect(gameDisplay,(4,12,25),[325,230,49,21])
        pygame.draw.rect(gameDisplay,(4,12,25),[309,270,82,21])
        enter = pygame.image.load('right-arrow.png')
        gameDisplay.blit(enter,(409,193))
        display_message(mode,350,281,17)
        display_message(str(score),350,241,17)
        display_message('RESTART',350,410,19)
        display_message('LEADERBOARD',350,445,19)
        display_message('MAIN MENU',350,480,19)
        #Checks if either 'RESTART','LEADERBOARD' or 'MAIN MENU' has been clicked, if they have the user is directed to the respective page; with all the previous game's data deleted
        if mouse[0] >= 317 and mouse[0] <= 384 and mouse[1] >= 403 and mouse[1] <= 416 and click[0] == 1:
            score = 0
            collision_player_count = 0
            alien_y = 85
            alien_x = 50
            ship_x = 350
            roundnum = 1
            for counter in range(0,48):
                a[counter] = 0
            game_over = False
            difficulty_selection = True
            name_entered = False
        elif mouse[0] >= 294 and mouse[0] <= 406 and mouse[1] >= 438 and mouse[1] <= 451 and click[0] == 1:
            score = 0
            collision_player_count = 0
            alien_const_y = 0
            alien_y = 85
            alien_x = 50
            ship_x = 350
            roundnum = 1
            for counter in range(0,48):
                a[counter] = 0
            game_over = False
            leaderboard = True
            name_entered = False
        elif mouse[0] >= 308 and mouse[0] <= 391 and mouse[1] >= 473 and mouse[1] <= 486 and click[0] == 1:
            score = 0
            collision_player_count = 0
            alien_const_y = 0
            alien_y = 85
            alien_x = 50
            ship_x = 350
            roundnum = 1
            for counter in range(0,48):
                a[counter] = 0
            game_over = False
            menu_exit = False
            name_entered = False

        #Check if the user has clicked on the box to enter their name, if they have the message "ENTER NAME" disappears and they are sent into a loop, and when they are done the message "DETAILS SAVED" is displayed
        if name_entered == False:
            if mouse[0] >= 312 and mouse[0] <= 418 and mouse[1] >= 190 and mouse[1] <= 210 and click[0] == 1:
                entering_name = True
            elif mouse[0] <= 312 or mouse[0] >= 418 or mouse[1] <= 259 or mouse[1] >= 279 or click[0] == 0:
                display_message('ENTER NAME',350,201,17)
        else:
            display_message('DETAILS SAVED',350,201,15)

        #This loop runs while the user is entering their name
        while entering_name == True:
            for event in pygame.event.get():
                #Lets the user input in the letters A to Z
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: name += 'A'
                    if event.key == pygame.K_b: name += 'B'
                    if event.key == pygame.K_c: name += 'C'
                    if event.key == pygame.K_d: name += 'D'
                    if event.key == pygame.K_e: name += 'E'
                    if event.key == pygame.K_f: name += 'F'
                    if event.key == pygame.K_g: name += 'G'
                    if event.key == pygame.K_h: name += 'H'
                    if event.key == pygame.K_i: name += 'I'
                    if event.key == pygame.K_j: name += 'J'
                    if event.key == pygame.K_k: name += 'K'
                    if event.key == pygame.K_l: name += 'L'
                    if event.key == pygame.K_m: name += 'M'
                    if event.key == pygame.K_n: name += 'N'
                    if event.key == pygame.K_o: name += 'O'
                    if event.key == pygame.K_p: name += 'P' 
                    if event.key == pygame.K_q: name += 'Q'
                    if event.key == pygame.K_r: name += 'R'  
                    if event.key == pygame.K_s: name += 'S'  
                    if event.key == pygame.K_t: name += 'T'  
                    if event.key == pygame.K_u: name += 'U' 
                    if event.key == pygame.K_v: name += 'V' 
                    if event.key == pygame.K_w: name += 'W'
                    if event.key == pygame.K_x: name += 'X'
                    if event.key == pygame.K_y: name += 'Y'
                    if event.key == pygame.K_z: name += 'Z'
                    if event.key == pygame.K_BACKSPACE: name = name[:-1]
                    
                    #Lets the user export the name,scores and the level of difficulty they just played in to the csv file by clicking the enter key
                    if event.key == pygame.K_RETURN:
                        with open('scores.csv','a+',newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([name,score,mode])
                            file.close()
                        entering_name = False
                        name_entered = True
                    #Limits the name to 7 characters
                    if len(name) > 7:
                        name = name[:-1]
                    
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            #Lets the user export the name,scores and modes to the csv file by clicking the enter button on the UI
            if mouse[0] >= 402 and mouse[0] <= 432 and mouse[1] >= 190 and mouse[1] <= 210 and click[0] == 1:
                with open('scores.csv','a+',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([name,score,mode])
                    file.close()
                entering_name = False
                name_entered = True
                
            #Displays a box and the name the user has typed in
            pygame.draw.rect(gameDisplay,(4,12,25),[300,190,100,21])
            display_message(name,350,201,17)
            pygame.display.update()
        pygame.display.update()

    #This loop runs while the user is on the leaderboard page
    while leaderboard == True:
        gameDisplay.blit(leaderboard_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaderboard = False
                game_exit = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #Imports the names,scores and modes from the csv
        with open("scores.csv","r") as f:
            reader = csv.reader(f,delimiter=",")
            names = []
            scores = []
            modes = []
            for row in reader:
                names.append(row[0])
                scores.append(row[1])
                modes.append(row[2])
            f.close()
            
        #Sorts out the names,scores and modes in descending order of scores using 2D arrays
        length = len(scores)
        data_to_display = [names,scores,modes]
        while length > 1:
            for x in range(0,(length - 1)):
                if int(data_to_display[1][x]) < int(data_to_display[1][x + 1]):
                    temp = data_to_display[1][x]
                    temp1 = data_to_display[0][x]
                    temp2 = data_to_display[2][x]
                    data_to_display[1][x] = data_to_display[1][x + 1]
                    data_to_display[1][x + 1] = temp
                    data_to_display[0][x] = data_to_display[0][x + 1]
                    data_to_display[0][x + 1] = temp1
                    data_to_display[2][x] = data_to_display[2][x + 1]
                    data_to_display[2][x + 1] = temp2
            length = length - 1
            
        #Displays the following items to the user interface
        display_message('SPACE INVADERS',350,40,50)
        display_message('LEADERBOARD',350,90,30)
        display_message("NAME",250,130,20)
        display_message("SCORE",375,130,20)
        display_message("MODE",500,130,20)
        display_message("1.",182,185,20)
        display_message("2.",183,215,20)
        display_message("3.",184,245,20)
        display_message("4.",183,275,20)
        display_message("5.",184,305,20)          
        display_message(data_to_display[0][0],250,185,20)
        display_message(data_to_display[0][1],250,215,20)
        display_message(data_to_display[0][2],250,245,20)
        display_message(data_to_display[0][3],250,275,20)
        display_message(data_to_display[0][4],250,305,20)
        display_message(data_to_display[1][0],375,185,20)
        display_message(data_to_display[1][1],375,215,20)
        display_message(data_to_display[1][2],375,245,20)
        display_message(data_to_display[1][3],375,275,20)
        display_message(data_to_display[1][4],375,305,20)
        display_message(data_to_display[2][0],500,185,20)
        display_message(data_to_display[2][1],500,215,20)
        display_message(data_to_display[2][2],500,245,20)
        display_message(data_to_display[2][3],500,275,20)
        display_message(data_to_display[2][4],500,305,20)
        display_message("MAIN MENU",610,40,20)
        
        #Checks if 'MAIN MENU' has been clicked, if it has then the user is directed to the main menu page
        if mouse[0] >= 563 and mouse[0] <= 657 and mouse[1] >= 33 and mouse[1] <= 46 and click[0] == 1:
            leaderboard = False
            menu_exit = False
        pygame.display.update()

    #This loop runs while the user is on the instructions page
    while instructions == True:
        gameDisplay.blit(instructions_bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False
                game_exit = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #Displays the following messages to the user interface
        display_message('SPACE INVADERS',350,80,50)
        display_message('INSTRUCTIONS',350,130,30)
        display_message('THE CONTROLS FOR THE GAME ARE:',189,210,20)
        display_message('PRESS RIGHT KEY TO MOVE RIGHT',235,240,20)
        display_message('PRESS LEFT KEY TO MOVE LEFT',223,270,20)
        display_message('PRESS SPACE TO SHOOT',194,300,20)
        display_message('PRESS THE P KEY TO PAUSE',208,330,20)
        display_message('FOR EVERY HIT ON AN ALIEN YOU GET 50 POINTS AND THE ALIENS START TO',351,360,20)
        display_message('SPEED UP EACH ROUND. FINALLY YOU GET 3 LIVES PER GAMES.',301,390,20)
        display_message('P.S. ENJOY THE GAME!!!',134,440,20)
        display_message("MAIN MENU",610,40,20)
        
        #Checks if 'MAIN MENU' has been clicked, if it has then the user is directed to the main menu page
        if mouse[0] >= 563 and mouse[0] <= 657 and mouse[1] >= 33 and mouse[1] <= 46 and click[0] == 1:
            instructions = False
            menu_exit = False
        pygame.display.update()

#Closes the module pygame
pygame.quit()
#Closes python
quit()
