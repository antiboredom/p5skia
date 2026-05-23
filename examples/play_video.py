from p5skia import Canvas

c = Canvas(show=True, fps=30)

vid = c.load_video("myvideo.mp4")
vid.loop = True

c.resize(vid.width, vid.height)

while c.draw():
    c.background(1, 1, 1)

    scale = 1
    c.image(vid.image, 0, 0, c.width, c.height)
    while scale > 0.1:
        scale -= 0.1
        c.push()
        c.translate(c.width / 2, c.height / 2)
        c.scale(scale)
        c.image(vid.image, -vid.width / 2, -vid.height / 2)
        c.pop()
    vid.next()
