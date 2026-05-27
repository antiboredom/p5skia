from imageio_ffmpeg import read_frames, count_frames_and_secs
import skia
import numpy as np
from typing import Iterator


class Video:
    path: str
    reader: Iterator
    meta: dict
    width: int
    height: int
    duration_frames: int | None
    duration_secs: float | None
    frame_number: int
    frames: list
    image: skia.Image
    loop: bool

    def __init__(self, path: str, loop: bool = False):
        self.path = path
        self.reader = read_frames(self.path, pix_fmt="rgb24")
        self.meta = self.reader.__next__()
        self.width = self.meta["size"][0]
        self.height = self.meta["size"][1]
        self.duration_frames = None
        self.duration_secs = None
        self.frame_number = 0
        self.frames = list(self.reader)
        self.loop = loop
        self.info()
        self.next()

    def info(self) -> tuple[int | None, float | None]:
        """Return the duration of the video in frames and seconds."""
        if not self.duration_frames:
            frames, secs = count_frames_and_secs(self.path)
            self.duration_frames = frames
            self.duration_secs = secs

        return self.duration_frames, self.duration_secs

    def next(self) -> None:
        """Advance to the next frame in the video and update the image attribute with the new frame data."""
        if self.frame_number < len(self.frames):
            self.frame = self.frames[self.frame_number]
            rgb_array = np.frombuffer(self.frame, dtype=np.uint8).reshape(
                (self.height, self.width, 3)
            )
            rgba_array = np.full((self.height, self.width, 4), 255, dtype=np.uint8)
            rgba_array[..., :3] = rgb_array
            self.image = skia.Image.fromarray(
                rgba_array,
            )
            self.frame_number += 1
        else:
            if self.loop:
                self.frame_number = 0

    # def next_old(self):
    #     if self.frame_number < self.duration_frames:
    #         self.frame = next(self.reader)
    #         rgb_array = np.frombuffer(self.frame, dtype=np.uint8).reshape(
    #             (self.height, self.width, 3)
    #         )
    #         rgba_array = np.full((self.height, self.width, 4), 255, dtype=np.uint8)
    #         rgba_array[..., :3] = rgb_array
    #         self.frame_number += 1
    #         # self.image = skia.Image.frombytes(
    #         #     self.frame,
    #         #     dimensions=(self.width, self.height),
    #         #     colorType=skia.kUnknown_ColorType,
    #         #     alphaType=skia.kOpaque_AlphaType,
    #         #     copy=False,
    #         # )
    #         self.image = skia.Image.fromarray(
    #             rgba_array,
    #         )
    #         # self.image = Image.frombytes(self.frame, (1280, 720))

    def skip_to(self, frame: int) -> None:
        """Skip to a specific frame number in the video."""

        self.frame_number = frame
        self.next()
