from p5skia import Canvas

c = Canvas(show=True, fps=30)

# load a video
vid = c.load_video("./examples/testvideo.mp4")

# loop it
vid.loop = True

# resize the canvas to make it the same dimensions of the video
c.resize(vid.width, vid.height)

while c.draw():
    c.background(1, 1, 1)

    scale = 1

    # display a frame from the video
    c.image(vid.image, 0, 0, c.width, c.height)

    # display multiple
    while scale > 0.1:
        scale -= 0.1
        c.push()
        c.translate(c.width / 2, c.height / 2)
        c.scale(scale)
        c.image(vid.image, -vid.width / 2, -vid.height / 2)
        c.pop()

    # go to the next frame
    vid.next()
