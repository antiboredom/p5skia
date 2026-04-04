from p5skia import Canvas

c = Canvas(width=600, height=600, show=True)

while c.draw():
    # set background to gray
    # all colors are rgba, 0.0 to 1.0
    c.background(0.9, 0.9, 0.9)

    # fill with rgb
    c.fill(1, 0, 0)
    # stroke with rgb
    c.stroke(0, 1, 0)
    # set stroke weight to be 3
    c.stroke_weight(3)
    # draw a rect
    c.rect(10, 10, 100, 100)

    # disable stroke
    c.no_stroke()
    c.fill(0.5, 0.2, 1)
    c.ellipse(100, 100, 50, 50)

    c.stroke(0, 0, 0)
    c.fill(0, 1, 0)
    c.triangle(300, 300, 350, 350, 325, 300)
