import sys
import cv2
from colours import BLOCK_SIZE, BLOCK_HOR, BLOCKS_VERT, EOF_INDEX, find_closest_index


def grab_frames(video_source):
    video = cv2.VideoCapture(video_source)

    image_list = []

    status, image = video.read()
    while status:
        rgb_image = image[..., ::-1].copy()  # convert bgr to rgb
        image_list.append(rgb_image)
        status, image = video.read()
    video.release()
    return image_list


def frame_to_list(frame):
    row_index = BLOCK_SIZE // 2
    col_index = BLOCK_SIZE // 2

    pixel_list = []
    for row_offset in range(BLOCKS_VERT):
        for col_offset in range(BLOCK_HOR):
            pixel_list.append(frame[row_index + row_offset * BLOCK_SIZE, col_index + col_offset * BLOCK_SIZE])
    return pixel_list


def decode(rgb_list):
    rgb_list = [x.tolist() for x in rgb_list]
    byte_list = []
    for i in range(0, len(rgb_list), 2):
        upper_nibble_value = find_closest_index(rgb_list[i])
        lower_nibble_value = find_closest_index(rgb_list[i + 1])
        if upper_nibble_value == EOF_INDEX & lower_nibble_value == EOF_INDEX:  # EOF Marker reached, stop
            break
        byte_value = (upper_nibble_value << 4) + lower_nibble_value
        byte = byte_value.to_bytes(1, byteorder=sys.byteorder)
        byte_list.append(byte)
    return byte_list


def decode_frames(frame_list):
    data = []
    for frame in frame_list:
        data.extend(decode(frame_to_list(frame)))
    return data
