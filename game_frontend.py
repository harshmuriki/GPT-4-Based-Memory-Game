import pygame
import numpy as np
import time
import game_backend


def random_array(num_grid, radius):
    array, images_dict = game_backend.backend(num_grid, radius)
    # print("arr", array)
    return array, images_dict


def iteration(num_grid=6):
    
    circle_radius = 20

    # get the random array
    global array, images_dict, coordinates, width
    width = 40
    array, images_dict = random_array(num_grid, circle_radius)
    
    # pygame setup
    pygame.init()
    # num_grid = 6
    screen = pygame.display.set_mode((1280, 720))
    screen.fill("pink")

    # Player1
    player1 = pygame.font.Font(None, 36)
    # Create a text surface
    player1_surface = player1.render('0', True, (255, 255, 255))
    global player1_rect
    player1_rect = player1_surface.get_rect()
    player1_rect.center = (1280*0.03, 50)

    # Player2
    player2 = pygame.font.Font(None, 36)
    player2_surface = player2.render('0', True, (255, 255, 255))
    global player2_rect
    player2_rect = player2_surface.get_rect()
    player2_rect.center = (1280*0.97, 50)

    # Player turn counter
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
    coordinates = np.zeros((num_grid, num_grid, 2)) #Global variable
    
    for i in range(pos_labels.shape[0]):
        for j in range(pos_labels.shape[1]):
            pos_labels[i, j, :] = pygame.Vector2(pos_x[i], pos_y[j])
            coordinates[i, j] = (pos_x[i], pos_y[j])

    # data = []
    data1 = []
    for i, val in enumerate(pos_labels):
        for j, pos_temp in enumerate(val):
            # print("loc", pos_temp)
            index = array[i, j]
            # print(color)
            # temp_pos = (pygame.Vector2(pos_temp[0], pos_temp[1]), "blue")
            # data.append(temp_pos)

            temp_pos1 = (pygame.Vector2(pos_temp[0], pos_temp[1]), 'white')
            data1.append(temp_pos1)

    # print(data)
    # data = np.array(data, dtype=tuple)
    data1 = np.array(data1, dtype=tuple)

    # positions = np.reshape(data, (num_grid, num_grid, 2))
    positions_white = np.reshape(data1, (num_grid, num_grid, 2))
    # print("pos", positions)

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
                mouse_pos = pygame.mouse.get_pos()
                for i in range(positions_white.shape[0]):
                    for j in range(positions_white.shape[1]):
                        circle_center = positions_white[i, j]
                        if ((mouse_pos[0] - circle_center[0][0]) ** 2 +
                                (mouse_pos[1] - circle_center[0][1]) ** 2) <= circle_radius ** 2:
                            circles_shown += 1
                            selected_circles.append((array[i, j], [i, j]))
                            
                            set_circles_to_image(screen, i, j, circle_radius)
                            
                            if circles_shown == 2:
                                time.sleep(1)
                                if selected_circles[0][0] == selected_circles[1][0]:
                                    num_finished += 1
                                    if turn == 1:
                                        player1_score += 1
                                        player1_surface, _ = set_player_score(
                                            screen, player1, player1_score, turn)
                                    elif turn == 2:
                                        player2_score += 1
                                        _, player2_surface = set_player_score(
                                            screen, player2, player2_score, turn)
                                    positions_white = set_circle_right(
                                        positions_white, selected_circles)
                                else:
                                    # if wrong selections
                                    set_wrong_selection(positions_white, screen, circle_radius, selected_circles)
                                circles_shown = 0
                                selected_circles = []
                                turn = 1 if turn == 2 else 2
                                temp_str = f"Player {turn} Turn"
                                player_turn_surface = player_turn.render(
                                    temp_str, True, (255, 255, 255))
                                pygame.draw.rect(
                                    screen, (0, 0, 0), player_turn_rect)
                            pygame.display.update()

        screen.blit(player1_surface, player1_rect)
        screen.blit(player2_surface, player2_rect)
        screen.blit(player_turn_surface, player_turn_rect)

        pygame.display.update()

        if num_finished == (num_grid**2) / 2:
            # go to a new screen
            if player1_score > player2_score:
                won_player = "Player 1 Won"
            elif player1_score == player2_score:
                won_player = "It was a tie"
            else:
                won_player = "Player 2 Won"
            # won_player = 1 if player1_score > player2_score else 2
            print(f"Game Results: {won_player}!!!!!!!!!!!!!!")
            # exit()
            break

    pygame.quit()


def set_circles_to_default(positions, screen, circle_radius):
    # print("Resetting all circles to default")
    for i in range(positions.shape[0]):
        for j in range(positions.shape[1]):
            x, y = positions[i, j][0]
            # print(x, y)
            # pygame.draw.circle(screen, "white", circle_center[0], circle_radius)
            pygame.draw.rect(screen, "white", (x - width/2, y-width/2, width, width))


def set_wrong_selection(positions, screen, circle_radius, selected_circles):

    for _, circle_center_idx in selected_circles:
        positions[circle_center_idx[0], circle_center_idx[1]][1] = "white"
        # print("center", positions[1])
        i, j = circle_center_idx
        # print(coordinates[i, j])
        x, y = coordinates[i, j]
        # pygame.draw.circle(screen, "white", coordinates[i, j], circle_radius)
        pygame.draw.rect(screen, "white", (x - width/2, y-width/2, width, width))


def set_circle_right(positions, selected_circles):
    for image, circle_center_idx in selected_circles:
        positions[circle_center_idx[0], circle_center_idx[1]][1] = "pink"
        
    return positions


def set_circles_to_color(circle_center, screen, circle_radius):
    # pygame.draw.circle(screen, circle_center[1], circle_center[0], circle_radius)
    pygame.draw.rect(screen, "white", pygame.Rect(5, 5))
    pygame.display.update()
    # print("Updated", circle_center[1])

def set_circles_to_image(screen, i, j, circle_radius):

    image = images_dict[array[i, j]]
    x, y = coordinates[i, j]
    loc = x - circle_radius, y - circle_radius
    
    screen.blit(image, loc, special_flags=pygame.BLEND_RGBA_MIN)

    pygame.display.update()

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
    iteration(4)
