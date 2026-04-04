from p5skia import Canvas

c = Canvas(width=600, height=600, show=True)

x = c.width / 2
y = c.height / 2
r = 100.0
xspeed = 1.1
yspeed = 2.4

while c.draw():
    c.background(0.9, 0.9, 0.9, 0.5)

    c.fill(0, 0, 0, 0.8)
    c.no_stroke()
    c.circle(x, y, r)

    x += xspeed
    y += yspeed

    if x + r >= c.width or x - r <= 0:
        xspeed *= -1

    if y + r >= c.height or y - r <= 0:
        yspeed *= -1
