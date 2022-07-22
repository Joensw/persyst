import cv2
import numpy as np
from Colours import colour_list, F_WIDTH, F_HEIGHT, BLOCK_SIZE, BLOCK_HOR, MAX_BLOCKS, EOF_INDEX

FPS = 6  # From testing this is seemingly the minimum FPS YouTube supports


def draw(colour_values):
    colour_values.extend([EOF_INDEX, EOF_INDEX])
    image_list = []
    image = np.zeros([F_HEIGHT, F_WIDTH, 3], dtype=np.uint8)
    count = 0
    for value in colour_values:
        row = count // BLOCK_HOR
        col = count % BLOCK_HOR
        image[row * BLOCK_SIZE:(row + 1) * BLOCK_SIZE, col * BLOCK_SIZE:(col + 1) * BLOCK_SIZE] = colour_list[value]
        count += 1
        if count >= MAX_BLOCKS:
            image_list.append(image)
            count = 0
            image = np.zeros([F_HEIGHT, F_WIDTH, 3], dtype=np.uint8)
    image_list.append(image)
    return image_list


def create_mp4_cv2(image_list, name):
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (F_WIDTH, F_HEIGHT))
    for image in image_list:
        rgb = image[..., ::-1].copy()  # open-cv uses the bgr colour format
        out.write(rgb)
    out.release()
