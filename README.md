# persyst

A small Python program to turn any file into an MP4 and back, by storing bytes as colour blocks.

It was created with the intention of seeing whether or not it would be possible to store data persistently on a platform like YouTube. Sadly in its current implementation the process is far too inefficient and slow for any meaningful practical use. The silly idea for it came to me after watching [this](https://www.youtube.com/watch?v=JcJSW7Rprio) rather excellent YouTube video.


## Installation

Use either the source code with command line arguments, or for windows use the executable file as shown below.


## Usage

There are two commands, encode and decode.

To turn a file into an MP4 use encode:

```
$ filetomp4.exe encode <filename.extension>
```
In the same directory as the source file you will now have an MP4 file which looks something like this:


<img src="https://user-images.githubusercontent.com/84239673/173181642-a41df83f-6584-44d7-898a-600cb1c6ac98.gif" width="40%" height="40%"/>

To turn an MP4 back into the original file use decode:

```
$ filetomp4.exe decode <filename.mp4> [--delete]
```
With the optional --delete flag, you can tell the program to delete the video file after decoding it.



## Further information

The program reads the bytes of a file, associates a colour with a certain byte and then draws a picture consisting of colour blocks, representing the original byte information of the file. These pictures are then used as frames to generate an Mp4. The process can naturally be reversed. One can even upload the video to YouTube, re-download it and still recover the information. 

When decoding an MP4 back into the original file, the extension is lost, so you will have to remember what type of file it was / with which programs you can open it.

The process of reading a file and generating a video from it / reversing it is rather slow. Files with a few 100KB will already take 10-20 seconds depending on the machine. Therefore, I cannot recommend trying to encode larger files.