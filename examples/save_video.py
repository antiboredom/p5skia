from p5skia import Canvas
import math

c = Canvas(width=600, height=600, renderer="GPU", show=False)

c.save_video("sketch_video1.mp4", fps=60)

while c.frame_count < 200:
    c.background(1, 1, 1)
    r = math.sin(c.frame_count / 50) * 100
    c.fill(0, 0, 0)
    c.ellipse(c.width / 2 - r / 2, c.height / 2 - r / 2, r, r)
    c.draw()

c.finish_video()
