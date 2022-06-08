F_WIDTH = 1280  # Width of the image frames
F_HEIGHT = 720  # Height of the image frame
BLOCK_SIZE = 16  # Size of the resulting colours blocks on the frames in pixels
BLOCKS_VERT = F_HEIGHT // BLOCK_SIZE  # Amount of blocks in a frame spanning vertically
BLOCK_HOR = F_WIDTH // BLOCK_SIZE  # Amount of blocks in a frame spanning horizontally
MAX_BLOCKS = BLOCKS_VERT * BLOCK_HOR  # Maximum amount of blocks in a frame
EOF_INDEX = 16  # Index of colour that serves as EOF Marker, must be >16

# List of rgb values used to save nibble information
# colours where chosen from: http://godsnotwheregodsnot.blogspot.com/2012/09/color-distribution-methodology.html
colour_list = [[0, 0, 0],
               [0, 255, 0],
               [0, 0, 255],
               [255, 0, 0],
               [1, 255, 254],
               [255, 156, 254],
               [255, 212, 102],
               [0, 100, 1],
               [1, 0, 103],
               [149, 0, 58],
               [0, 125, 181],
               [255, 0, 246],
               [255, 238, 232],
               [119, 77, 0],
               [144, 251, 146],
               [0, 118, 255],
               [67, 0, 44]]


def absolute_difference(list1, list2):
    subtracted = list()
    for item1, item2 in zip(list1, list2):
        item = item1 - item2
        subtracted.append(abs(item))
    return sum(subtracted)


def find_closest_index(bgr_values):
    match_index = 0
    shortest_distance = absolute_difference(bgr_values, colour_list[match_index])
    for i in range(len(colour_list)):
        cur_rgb = colour_list[i]
        cur_distance = absolute_difference(cur_rgb, bgr_values)
        if cur_distance < shortest_distance:
            shortest_distance = cur_distance
            match_index = i
    return match_index
