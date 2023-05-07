import numpy as np


def backend(size):
    grid_size = [size, size]  # only even no

    number_words = (grid_size[0] * grid_size[1]) // 2

    arr = ['#FF3E4D', '#41EAD4', '#364F6B', '#F5F1ED', '#D7263D', '#98C1D9', '#4F9D69', '#E2C044', '#3F5D7D', '#FF8360', '#49BEAA', '#26547C', '#F0E5D8', '#DC3023', '#2F6690',
            '#9BC53D', '#FFC09F', '#2F2D2E', '#FFA62B', '#4F3836', '#5D3A9B', '#8F2D56', '#8E5572', '#95DEE3', '#C1D37F', '#8CBEB2', '#E8DBA8', '#4A7C59', '#F18805', '#D8A7B1']

    words = np.array(arr)

    chosen_words = np.random.choice(words, number_words, False)
    # print(chosen_words)

    one_arr = np.random.choice(np.arange(0, number_words),
                               size=number_words, replace=False)

    grid_1d = np.concatenate((one_arr, one_arr))
    np.random.shuffle(grid_1d)

    grid_empty = grid_1d.reshape(grid_size)
    
    random_final_grid = chosen_words[grid_empty]

    return random_final_grid
