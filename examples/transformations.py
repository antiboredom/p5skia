from p5skia import Canvas

c = Canvas(width=600, height=600, show=True)

while c.draw():
    c.background(0.9, 0.9, 0.9)

    c.fill(1, 0, 0)

    c.push()
    c.translate(c.width / 2, c.height / 2)
    c.scale(2, 2)
    c.rotate(100)
    c.rect(0, 0, 100, 100)
    c.pop()

    # you can also use 'with'

    with c.state():
        c.translate(100, 10)
        c.scale(1.5, 1.5)
        c.rect(0, 0, 50, 100)

    c.rect(0, 0, 10, 10)
