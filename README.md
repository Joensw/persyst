# persyst

A Python program to turn an arbitrary file into an MP4 and back, by storing bytes as colour blocks.

It was created with the intention of seeing whether it would be possible to store data persistently on a platform like YouTube. It works as intended, but should be seen as a proof of concept. The silly idea for it came to me after watching an excellent YouTube video on [Harder Drives](https://www.youtube.com/watch?v=JcJSW7Rprio).


## Requirements and Installation

Clone the repository or download it as a zip and extract it.

The necessary python packages that are needed are listed in the requirements.txt file.

They can be installed manually or with the command `pip install -r requirements.txt`.



## Usage

There are two commands, encode and decode.

To turn a file into an MP4 use encode:

```
$ python main.py encode <filename.extension>
```
In the same directory as the source file you will now have an MP4 file which looks something like this:


<img src="https://user-images.githubusercontent.com/84239673/173181642-a41df83f-6584-44d7-898a-600cb1c6ac98.gif" width="40%" height="40%"/>

To turn an MP4 back into the original file use decode:

```
$ python main.py decode <filename.mp4> [--delete]
```
With the optional --delete flag, you can tell the program to delete the video file after decoding it.

### YouTube

Using these two commands you can store files persistently on YouTube by uploading the encoded video, and redownloading and decoding it when you want to use it


## Further information

The program reads the bytes of a file, associates a colour with a certain byte and then draws a picture consisting of colour blocks, representing the original byte information of the file. These pictures are then used as frames to generate a MP4. The process can naturally be reversed. One can even upload the video to YouTube, re-download it and still recover the information. 

The output video will be significantly larger than the input file, in my testing this is usually around 6-10x, which is alright but not great. This could probably be reduced by increasing the FPS or reducing the block size, I have not optimized either of these parameters and basically set them arbitrarily to 6 FPS and 16x16 blocks.

Encoding a 1MB file takes around 10 seconds, and decoding the encoded files takes about 30 seconds. This is on my machine, performance on your machine will vary. However, while these numbers aren't terrible I cannot recommend trying to large files as it will probably take a very long time.

When decoding an MP4 back into the original file, the extension is lost, so you will have to remember what type of file it was / with which programs you can open it.

