import numpy as np

grid_size = [4, 4]  # only even no

number_words = (grid_size[0] * grid_size[1]) // 2

words = np.array(['Red', 'Blue', 'Green', 'Yellow', 'Purple',
                  'Orange', 'Pink', 'Brown', 'Gray', 'Black'])

chosen_words = np.random.choice(words, number_words, False)
# print(chosen_words)

one_arr = np.random.choice(np.arange(0, number_words),
                           size=number_words, replace=False)

grid_1d = np.concatenate((one_arr, one_arr))
np.random.shuffle(grid_1d)

grid_empty = grid_1d.reshape(grid_size)
# print(grid)

# [['Green' 'Orange' 'Purple' 'Yellow']
#  ['Red' 'Gray' 'Red' 'Purple']
#  ['Blue' 'Green' 'Gray' 'Yellow']
#  ['Pink' 'Orange' 'Pink' 'Blue']]
random_final_grid = chosen_words[grid_empty]
