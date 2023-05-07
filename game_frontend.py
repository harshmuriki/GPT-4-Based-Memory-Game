import pygame
import numpy as np
import time
import game_backend


def random_array(num_grid):
    array = game_backend.backend(num_grid)
    return array


def iteration():
    # pygame setup
    pygame.init()
    num_grid = 6
    screen = pygame.display.set_mode((1280, 720))

    # get the random array
    global array
    array = random_array(num_grid)
    screen.fill("pink")

    # Player1
    player1 = pygame.font.Font(None, 36)
    # Create a text surface
    player1_surface = player1.render('0', True, (255, 255, 255))
    global player1_rect
    player1_rect = player1_surface.get_rect()
    player1_rect.center = (1280*0.03, 50)

    # player2
    player2 = pygame.font.Font(None, 36)
    player2_surface = player2.render('0', True, (255, 255, 255))
    global player2_rect
    player2_rect = player2_surface.get_rect()
    player2_rect.center = (1280*0.97, 50)

    # player turn shower
    player_turn = pygame.font.Font(None, 25)
    player_turn_surface = player_turn.render(
        'Player 1 Turn', True, (255, 255, 255))
    global player_turn_rect
    player_turn_rect = player_turn_surface.get_rect()
    player_turn_rect.center = (1280*0.50, 50)

    running = True

    pos_x = np.linspace(
        screen.get_width() * 0.1, screen.get_width() * 0.9, num_grid)
    pos_y = np.linspace(
        screen.get_height() * 0.1, screen.get_height() * 0.9, num_grid)

    pos_labels = np.zeros((num_grid, num_grid, 2))

    for i in range(pos_labels.shape[0]):
        for j in range(pos_labels.shape[1]):
            pos_labels[i, j, :] = pygame.Vector2(pos_x[i], pos_y[j])

    data = []
    data1 = []
    for i, val in enumerate(pos_labels):
        for j, pos_temp in enumerate(val):
            # print("loc", pos_temp)
            color = array[i, j]
            # print(color)
            temp_pos = (pygame.Vector2(pos_temp[0], pos_temp[1]), color)
            data.append(temp_pos)

            temp_pos1 = (pygame.Vector2(pos_temp[0], pos_temp[1]), 'white')
            data1.append(temp_pos1)

    # print(data)
    data = np.array(data, dtype=tuple)
    data1 = np.array(data1, dtype=tuple)

    positions = np.reshape(data, (num_grid, num_grid, 2))
    positions_white = np.reshape(data1, (num_grid, num_grid, 2))
    # print("pos", positions)
    circle_radius = 20

    # Draw inital circles
    set_circles_to_default(positions_white, screen, circle_radius)

    circles_shown = 0
    turn = 1
    selected_circles = []
    player1_score = 0
    player2_score = 0
    num_finished = 0
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                # print("Player {0}'s Turn".format(turn))
                mouse_pos = pygame.mouse.get_pos()
                # print(mouse_pos)
                for i in range(positions.shape[0]):
                    for j in range(positions.shape[1]):
                        center = positions[i, j]
                        if ((mouse_pos[0] - center[0][0]) ** 2 +
                                (mouse_pos[1] - center[0][1]) ** 2) <= circle_radius ** 2:
                            # Change the color of the clicked circle to blue
                            circles_shown += 1
                            selected_circles.append((center[1], [i, j]))
                            # print("Circles:", circles_shown)
                            set_circles_to_color(
                                positions[i, j], screen, circle_radius)
                            if circles_shown == 2:
                                time.sleep(1)
                                if selected_circles[0][0] == selected_circles[1][0]:
                                    # print("Showing the chosen choices")
                                    num_finished += 1
                                    if turn == 1:
                                        # print("Player 1 wins")
                                        player1_score += 1
                                        player1_surface, _ = set_player_score(
                                            screen, player1, player1_score, turn)
                                    elif turn == 2:
                                        player2_score += 1
                                        # print("Player 2 wins")
                                        _, player2_surface = set_player_score(
                                            screen, player2, player2_score, turn)
                                    set_circle_right(
                                        positions_white, selected_circles)

                                set_circles_to_default(
                                    positions_white, screen, circle_radius)
                                circles_shown = 0
                                # score(turn, selected_circles)
                                selected_circles = []
                                turn = 1 if turn == 2 else 2
                                temp_str = f"Player {turn} Turn"
                                player_turn_surface = player_turn.render(
                                    temp_str, True, (255, 255, 255))
                                pygame.draw.rect(
                                    screen, (0, 0, 0), player_turn_rect)

                                # circles_shown = 0
                            pygame.display.update()

        screen.blit(player1_surface, player1_rect)
        screen.blit(player2_surface, player2_rect)
        screen.blit(player_turn_surface, player_turn_rect)

        pygame.display.update()

        if num_finished == (num_grid**2) / 2:
            # go to a new screen
            if player1_score > player2_score:
                won_player = 1
            elif player1_score == player2_score:
                won_player = "tie"
            else:
                won_player = 2
            won_player = 1 if player1_score > player2_score else 2
            print(f"Game won by player {won_player}!!!!!!!!!!!!!!")
            exit()

    pygame.quit()


def set_circles_to_default(positions, screen, circle_radius):
    # print("Resetting all circles to default")
    for i in range(positions.shape[0]):
        for j in range(positions.shape[1]):
            center = positions[i, j]
            pygame.draw.circle(screen, center[1], center[0], circle_radius)


def set_circle_right(positions, centers):
    for color, center_idx in centers:
        positions[center_idx[0], center_idx[1]][1] = color


def set_circles_to_color(center, screen, circle_radius):
    pygame.draw.circle(screen, center[1], center[0], circle_radius)
    pygame.display.update()
    # print("Updated", center[1])


def set_player_score(screen, player, score, turn):
    score = str(score)
    player_surface = player.render(score, True, (255, 255, 255))

    if turn == 1:
        pygame.draw.rect(screen, (0, 0, 0), player1_rect)
        return player_surface, None
    else:
        pygame.draw.rect(screen, (0, 0, 0), player2_rect)
        return None, player_surface


if __name__ == "__main__":
    iteration()
    # array = random_array()
    # print(array)
