from PIL import Image
import numpy as np
import random

def sum2DArray(array):
    total = 0
    for i in array:
        for j in i:
            total += j
    return total

img = Image.open('penguin.jpg').convert('L')
pixel_array = img.load()

width, height = img.size
window_size = (19, 19)
window_matrix = [[(1/361) for i in range(window_size[0])] for i in range(window_size[1])]
image_window_matrix = []
image_window_matrix_row = []


for x in range(int(((window_size[0]-1)/2)), width-int(((window_size[0]-1)/2))):
    for y in range(int(((window_size[1]-1)/2)), height-int(((window_size[1]-1)/2))):
        image_window_matrix = []
        for j in range((y - int(((window_size[1]-1)/2))), ((y + int(((window_size[1]-1)/2)))+1)):
            image_window_matrix_row = []
            for i in range((x - int(((window_size[0] - 1) / 2))), ((x + int(((window_size[0] - 1) / 2))) + 1)):
                image_window_matrix_row.append(pixel_array[i, j])
            image_window_matrix.append(image_window_matrix_row)

        image_window_matrix = np.array(image_window_matrix)
        window_matrix = np.array(window_matrix)

        outputPixelArray = image_window_matrix * window_matrix
        print(x,y)
        pixel_array[x, y] = int(sum2DArray(outputPixelArray))


print("done")
img.save('applied_penguin.png')




