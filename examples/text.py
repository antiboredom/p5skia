from p5skia import Canvas

c = Canvas(width=600, height=600, show=True)

while c.draw():
    c.background(0.9, 0.9, 0.9)

    c.no_stroke()
    c.fill(0, 0, 0)

    c.text_font("Helvetica")

    c.text_size(10)
    c.text("Hello!", 20, 20)

    c.text_size(50)
    c.text("Hello!", 20, 100)

    c.text_font("Times New Roman")
    c.text("Helllloooo", 20, 200)

    c.text_size(15)
    c.text("Multi\nline\nText", 20, 300)

    c.text_size(20)
    c.text_style("bolditalic")
    c.text("Bold italic text", 20, 400)
