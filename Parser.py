import pathlib
import argparse

encode_command = "encode"
encode_src = "src_file"

decode_command = "decode"
decode_src = "src_file"
decode_del = "delete"


def source_file(path):
    p = pathlib.Path(path)
    if p.is_file():
        return path
    else:
        raise argparse.ArgumentTypeError(f"the path {path} is not valid, or not a file")


def parse():
    parser = argparse.ArgumentParser(description="Convert a file into a visual representation as an MP4 an back")

    subparsers = parser.add_subparsers(dest="command_name", title="Commands",
                                       description="Valid commands the program offers")

    parser_encode = subparsers.add_parser(encode_command,
                                          help="Store bytes from a file as colour blocks in an MP4")

    parser_encode.add_argument(encode_src, type=source_file, help="Path to a file which is used as the source")

    parser_decode = subparsers.add_parser(decode_command,
                                          help="Revert an MP4 from a previous encode back into the original file")

    parser_decode.add_argument(decode_src, type=source_file, help="Path to the MP4 file that is to be converted back")
    parser_decode.add_argument(f"--{decode_del}", help="Delete the MP4 file after decoding it", action="store_true")

    return parser.parse_args()
