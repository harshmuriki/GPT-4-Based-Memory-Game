import pygame
import numpy as np
import time
import game_backend
import main_screen
import sys


def init_screen():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Memory Game")

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define text box properties
    prompt_rect = pygame.Rect(100, 250, 200, 30)
    size_rect = pygame.Rect(100, 350, 200, 30)
    font = pygame.font.Font(None, 24)
    font_top = pygame.font.Font(None, 24)
    prompt = ''
    size = ''

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Entered text 1:", prompt)
                    print("Entered text 2:", size)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    if prompt_rect.collidepoint(pygame.mouse.get_pos()):
                        prompt = prompt[:-1]
                    elif size_rect.collidepoint(pygame.mouse.get_pos()):
                        size = size[:-1]
                else:
                    if prompt_rect.collidepoint(pygame.mouse.get_pos()):
                        prompt += event.unicode
                    elif size_rect.collidepoint(pygame.mouse.get_pos()):
                        size += event.unicode

        screen.fill("pink")

        # Draw the text boxes
        pygame.draw.rect(screen, BLACK, prompt_rect, 2)
        pygame.draw.rect(screen, BLACK, size_rect, 2)

        # Welcome text
        welcome_text = font.render("Welcome to the Memory Game", True, BLACK)
        screen.blit(welcome_text, (300, 100))

        # Render and display the input text for textbox1
        text_surface1 = font.render(prompt, True, BLACK)
        prompt_text = font.render(
            "Enter the topic of the memory game. Eg: Colors, Cars, planes, etc.", True, BLACK)
        screen.blit(prompt_text, (prompt_rect.x, prompt_rect.y - 20))
        screen.blit(text_surface1, (prompt_rect.x + 5, prompt_rect.y + 5))

        # Render and display the input text for textbox2
        text_surface2 = font.render(size, True, BLACK)
        size_text = font.render(
            "Enter the size of the grid you want. It can only be positive, even numbers. Eg: 2, 4, 6, 8, 10", True, BLACK)
        screen.blit(size_text, (size_rect.x, size_rect.y - 20))
        screen.blit(text_surface2, (size_rect.x + 5, size_rect.y + 5))

        # Return text
        return_text = font.render(
            "Press enter to go to the game screen", True, BLACK)
        screen.blit(return_text, (300, 500))

        pygame.display.flip()

    pygame.quit()
    # sys.exit()

    return (prompt, int(size))


def game_screen(prompt, size):
    player_won = main_screen.iteration(prompt, size)

    return player_won


def end_screen(player_won):
    # Show who won

    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Memory Game Game Finished")

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define text box properties
    prompt_rect = pygame.Rect(100, 250, 200, 30)
    size_rect = pygame.Rect(100, 350, 200, 30)
    font = pygame.font.Font(None, 24)
    prompt = ''
    size = ''

    # Return text
    text = ""
    if player_won == 0:
        text = "The game was a tie!!"
    else:
        text = "Player {:} won the game!!!".format(player_won)

    return_text = font.render(text, True, BLACK)

    regame = False
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    regame = True

        screen.blit(return_text, (300, 200))

        screen.fill("pink")

        pygame.display.flip()

    pygame.quit()

    return regame


def end_screen(player_won):
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Memory Game Game Finished")

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define font properties
    font = pygame.font.Font(None, 36)

    # Return text
    text = ""
    if player_won == 0:
        text = "The game was a tie!!"
    else:
        text = "Player {:} won the game!!!".format(player_won)

    print(text)

    # Render the text
    text = font.render(text, True, BLACK)

    # Get the text's width and height
    text_width = text.get_width()
    text_height = text.get_height()

    # Calculate the position to center the text on the screen
    text_x = (screen.get_width() - text_width) // 2
    text_y = (screen.get_height() - text_height) // 2

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("pink")

        # Display the text on the screen
        screen.blit(text, (text_x, text_y))

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


def main():

    prompt = ""
    size = -1

    while size < 0:
        prompt, size = init_screen()

        if size % 2 == 1:
            size = -1

    player_won = game_screen(prompt, size)

    regame = end_screen(player_won)

    if regame:
        main()
    else:
        return


if __name__ == "__main__":
    main()
