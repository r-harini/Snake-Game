import pygame
import time
import random
#initialize all the pygame modules
pygame.init()

#to create the surface
dis_width=600
dis_height=400
dis=pygame.display.set_mode((dis_width, dis_height))

#updates the screen
#pygame.display.update()

pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block=10
snake_speed=15

clock=pygame.time.Clock()


font_style=pygame.font.SysFont("bahnschrift",25)
score_font=pygame.font.SysFont("comicsansms",35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6, dis_height/3])

def gameLoop():
    game_over=False
    game_close=False
    
    x1= dis_width/2
    y1= dis_height/2

    dx1=0
    dy1=0

    snake_list=[]
    Length_of_snake=1

    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    #loop to keep rendering the screen
    while not game_over:
        while game_close==True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q or event.key==pygame.QUIT:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameLoop()
        #collect any keybpard/mouse event performed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    dx1=0
                    dy1= snake_block
                elif event.key == pygame.K_UP:
                    dx1=0
                    dy1= -snake_block
                elif event.key == pygame.K_LEFT:
                    dx1=-snake_block
                    dy1=0
                elif event.key == pygame.K_RIGHT:
                    dx1= snake_block
                    dy1=0
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
        x1+=dx1
        y1+=dy1
        dis.fill(white)

        #to draw the rectangular snake
        pygame.draw.rect(dis,green,[foodx,foody, snake_block,snake_block])

        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_list)
        Your_score(Length_of_snake - 1)

        #pygame.draw.rect(dis,black,[x1,y1,10,10])
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    
    #time.sleep(2)
    #to uninitialize everything
    pygame.quit()
    quit()
gameLoop()