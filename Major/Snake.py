import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
cyan = (0, 255, 255)
light_green = (144, 238, 144)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

# Display dimensions
display_width = 600
display_height = 400

# Initialize the game display
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Vedant')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Set the font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 20)  # Smaller font size for the score

def our_snake(snake_block, snake_List):
    for i, x in enumerate(snake_List):
        color = cyan if i % 2 == 0 else light_green
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

def your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [10, 10])  # Position the score at the top-left corner

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    direction = None

    while not game_over:
        while game_close:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)  # Display the score (Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y1_change = snake_block
                    x1_change = 0
                    direction = "DOWN"

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        snake_head_color = cyan if len(snake_List) % 2 == 0 else light_green
        food_color = light_green if snake_head_color == cyan else cyan

        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)  # Display the score (Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
