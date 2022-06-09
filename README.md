# FileToMP4

A small Python program to turn any file into an MP4 and back. 

It was created mainly to learn the basics of python, but the original idea was to use it to store data persistently on a platform like YouTube. That quickly turned out to be unfeasible as it is far too inefficient and slow for any meaningful practical use. The silly idea for it came to me after watching [this](https://www.youtube.com/watch?v=JcJSW7Rprio) rather excellent YouTube video.

## Installation

Install the source code and use with command line arguments, or for windows use the executable file as shown below


## Usage

There are two commands, encode and decode.

To turn a file into an MP4 use encode:

```
$ filetomp4.exe encode <filename.extension>
```

To turn an MP4 back into the original file use decode:

```
$ filetomp4.exe decode <filename.mp4> [--delete]
```
With the optional --delete flag, you can tell the program to delete the video file after decoding it.

## Demo

https://user-images.githubusercontent.com/84239673/172876137-77b5c1bf-49ae-4ed1-b741-24562b75cb16.mp4


As the video shows, converting even just a ~300KB file already takes a significant amount of time
