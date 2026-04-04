from p5skia import Canvas

c = Canvas(width=600, height=600, show=False)
c.fill(1, 0, 0)
c.stroke(0, 0, 1)
c.stroke_weight(10)
c.rect(c.width / 2, c.height / 2, 100, 100)
c.save("sketch1.png")
