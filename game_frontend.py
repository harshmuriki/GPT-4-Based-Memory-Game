import pygame
import numpy as np


def iteration():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    player1 = pygame.font.Font(None, 36)
    # Create a text surface
    player1_surface = player1.render('0', True, (255, 255, 255))
    player1_rect = player1_surface.get_rect()
    player1_rect.center = (1280*0.03, 50)

    # player2
    player2 = pygame.font.Font(None, 36)
    player2_surface = player2.render('0', True, (255, 255, 255))
    player2_rect = player2_surface.get_rect()
    player2_rect.center = (1280*0.97, 50)  # screen.get_rect().bottomright

    running = True
    num_grid = 4

    pos_x = np.linspace(
        screen.get_width() * 0.1, screen.get_width() * 0.9, num_grid)
    pos_y = np.linspace(
        screen.get_height() * 0.1, screen.get_height() * 0.9, num_grid)

    pos_labels = np.zeros((num_grid, num_grid, 2))

    for i in range(pos_labels.shape[0]):
        for j in range(pos_labels.shape[1]):
            pos_labels[i, j, :] = pygame.Vector2(pos_x[i], pos_y[j])

    data = []
    for i in pos_labels:
        for pos_temp in i:
            # print("loc", pos_temp)
            temp_pos = (pygame.Vector2(pos_temp[0], pos_temp[1]), "white")
            data.append(temp_pos)

    # print(data)
    data = np.array(data)

    positions = np.reshape(data, (num_grid, num_grid, 2))
    # print("pos", positions)
    circle_radius = 20

    # Draw inital circles
    set_circles_to_white(positions, screen, circle_radius)

    circles_shown = 0
    turn = 1
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                print("Player {0}'s Turn".format(turn))
                mouse_pos = pygame.mouse.get_pos()
                # print(mouse_pos)
                for i in range(positions.shape[0]):
                    for j in range(positions.shape[1]):
                        center = positions[i, j]
                        if ((mouse_pos[0] - center[0][0]) ** 2 +
                                (mouse_pos[1] - center[0][1]) ** 2) <= circle_radius ** 2:
                            # Change the color of the clicked circle to blue
                            if circles_shown == 2:
                                set_circles_to_white(
                                    positions, screen, circle_radius)
                                circles_shown = 0
                                turn = 1 if turn == 2 else 2

                            circles_shown += 1
                            i, j = np.unravel_index(np.where(positions == center)[
                                                    0][0], positions.shape[:2])
                            positions[i, j] = (center[0], "blue")
                            # print("Yes")
                            # print(positions)
                            pygame.display.update()

        for i in range(positions.shape[0]):
            for j in range(positions.shape[1]):
                center = positions[i, j]
                if center[1] == 'blue':
                    # print(center)
                    pygame.draw.circle(
                        screen, center[1], center[0], circle_radius)

        screen.blit(player1_surface, player1_rect)
        screen.blit(player2_surface, player2_rect)

        pygame.display.update()

    pygame.quit()


def set_circles_to_white(positions, screen, circle_radius):
    for i in range(positions.shape[0]):
        for j in range(positions.shape[1]):
            center = positions[i, j]
            pygame.draw.circle(screen, center[1], center[0], circle_radius)


if __name__ == "__main__":
    iteration()
