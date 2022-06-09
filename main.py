import os
import ByteConverter
import ImageGenerator
import ImageDecoder
from Parser import parse, encode_command, decode_command, encode_src, decode_src, decode_del


def encode(input_file):
    input_nibbles = ByteConverter.read_nibbles(input_file)
    image_list = ImageGenerator.draw(input_nibbles)
    ImageGenerator.create_mp4_cv2(image_list, f"{input_file}ENCODED")


def decode(input_video, delete_after):
    frame_list = ImageDecoder.grab_frames(input_video)
    byte_list = ImageDecoder.decode_frames(frame_list)
    ByteConverter.write_bytes(f"{input_video}DECODED", byte_list)
    if delete_after:
        os.remove(input_video)


def main():
    args = parse()
    varargs = vars(args)
    if args.command_name == encode_command:
        encode(varargs[encode_src])
    if args.command_name == decode_command:
        decode(varargs[decode_src], varargs[decode_del])


if __name__ == '__main__':
    main()
