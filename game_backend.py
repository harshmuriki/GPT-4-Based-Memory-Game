import numpy as np
import gpt3_color
import requests
from io import BytesIO
import gpt3_image
import pygame


def backend(size, radius, prompt):

    grid_size = [size, size]  # only even no

    number_words = (grid_size[0] * grid_size[1]) // 2

#     arr = ['#FF3E4D', '#41EAD4', '#364F6B', '#F5F1ED', '#D7263D', '#98C1D9', '#4F9D69', '#E2C044', '#3F5D7D', '#FF8360', '#49BEAA', '#26547C', '#F0E5D8', '#DC3023', '#2F6690',
#             '#9BC53D', '#FFC09F', '#2F2D2E', '#FFA62B', '#4F3836', '#5D3A9B', '#8F2D56', '#8E5572', '#95DEE3', '#C1D37F', '#8CBEB2', '#E8DBA8', '#4A7C59', '#F18805', '#D8A7B1']

#     arr = gpt3_color.prompt(int(size*size*0.70) + 2)
#     print(arr)
    print("Getting the images from GPT")
    links = gpt3_image.prompt(number_words, prompt)

    # links = ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-dZcEmqV4WTGc8KyvoaKKdtso/user-3xDZBl4STWUXMYfZRINHE7Cn/img-TCWFi5UShuZCtZyk7y1dv6Ny.png?st=2023-05-12T23%3A22%3A00Z&se=2023-05-13T01%3A22%3A00Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-05-12T20%3A39%3A22Z&ske=2023-05-13T20%3A39%3A22Z&sks=b&skv=2021-08-06&sig=cJ8jQ5ZQ6%2BosA/meSX0QKBU18QpfRgDZnpnXBeD%2BEa8%3D',
    #          'https://oaidalleapiprodscus.blob.core.windows.net/private/org-dZcEmqV4WTGc8KyvoaKKdtso/user-3xDZBl4STWUXMYfZRINHE7Cn/img-R9YyMTylw3Yc2MVRGdIi43L3.png?st=2023-05-12T23%3A22%3A00Z&se=2023-05-13T01%3A22%3A00Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-05-12T20%3A39%3A22Z&ske=2023-05-13T20%3A39%3A22Z&sks=b&skv=2021-08-06&sig=KRG4Um6qTq6ewdwNH%2BhkEs51yjjJ%2BRXo0Dog3iSYvNg%3D']

    # print("Links:", links)
    print("Got the images")
    images_dict = convt_img(links, radius)

    chosen_words = np.random.choice(len(links), number_words, False)
    # print(chosen_words)

    one_arr = np.random.choice(np.arange(0, number_words),
                               size=number_words, replace=False)

    grid_1d = np.concatenate((one_arr, one_arr))
    np.random.shuffle(grid_1d)

    grid_empty = grid_1d.reshape(grid_size)

    random_final_grid = chosen_words[grid_empty]

    return random_final_grid, images_dict


def convt_img(data, radius):

    # size = len(data)/2
    # images = np.empty((size,size,2))
    # print(images.shape)

    images = {}

    for index, link in enumerate(data):
        response = requests.get(link)
        image_data = response.content

        # Load the image into Pygame
        temp_img = pygame.image.load(BytesIO(image_data))
        # resized_image = pygame.transform.scale(temp_img, (30, 30))
        
        # Scale and blit the square image onto the circular surface
        scaled_image = pygame.transform.scale(temp_img, (radius * 2, radius * 2))

        images[index] = (scaled_image)

    # print(images)
    return images


if __name__ == "__main__":
    ar = backend(2)

    print(ar)
