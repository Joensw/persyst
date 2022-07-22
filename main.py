import ByteConverter
import ImageGenerator
import ImageDecoder
import uploader

import os

from types import SimpleNamespace
from pathlib import Path
from Parser import parse, encode_command, decode_command, encode_src, encode_upload, decode_src, decode_del
from googleapiclient.errors import HttpError


def encode(input_file, upload_after):
    input_nibbles = ByteConverter.read_nibbles(input_file)
    image_list = ImageGenerator.draw(input_nibbles)
    video_file = f"{input_file}ENCODED.mp4"
    ImageGenerator.create_mp4_cv2(image_list, video_file)

    original_file_type = Path(input_file).suffix
    if upload_after:
        upload(video_file, original_file_type)


def decode(input_video, delete_after):
    frame_list = ImageDecoder.grab_frames(input_video)
    byte_list = ImageDecoder.decode_frames(frame_list)
    ByteConverter.write_bytes(f"{input_video}DECODED", byte_list)
    if delete_after:
        os.remove(input_video)


def upload(src_file, file_type):
    src_path = Path(src_file)
    pseudo_args = SimpleNamespace(file=src_file, title=src_file, description=file_type, category="22",
                                  keywords="",
                                  privacyStatus="private")
    if not src_path.exists():
        exit("Couldn't find video to upload!")
    youtube = uploader.get_authenticated_service(pseudo_args)
    try:
        uploader.initialize_upload(youtube, pseudo_args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))


def main():
    args = parse()
    varargs = vars(args)
    if args.command_name == encode_command:
        encode(varargs[encode_src], varargs[encode_upload])
    if args.command_name == decode_command:
        decode(varargs[decode_src], varargs[decode_del])


if __name__ == '__main__':
    main()
