# p5skia

A quick, very very work-in-progress library that lets you draw with Skia in Python in a Processing-style way, with many functions borrowed from p5py's skia renderer. I use it in my own work for quick procedural video/pdf/image generation, but its not really ready yet for general consumption.

Documentation can be find in [docs.md](docs.md).

Take a look at the examples folder for basic usage.

## Goals & Non-Goals:

### Goals

- simple, p5/processing-like api for skia
- more "pythony" than p5py, and exposes more skia stuff
- good for exporting animation as video files, images, and pdfs suitable for printing
- can be headless

### Non-Goals

- user interaction (mouse/keyboard/etc)
- audio
