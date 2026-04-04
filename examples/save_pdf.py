from p5skia import Canvas

# dimensions at 72dpi for a 8.5x11 inch page
page_width = int(72 * 8.5)
page_height = int(72 * 11)

c = Canvas(
    width=page_width, height=page_height, renderer="PDF", output="single_page.pdf"
)
c.background(1, 1, 1)
c.fill(1, 0, 0)
c.stroke(0, 0, 1)
c.stroke_weight(10)
c.rect(100, 100, 100, 100)
c.save_pdf()

c = Canvas(
    width=page_width, height=page_height, renderer="PDF", output="multi_page.pdf"
)
c.background(1, 1, 1)
c.rect(100, 100, 120, 150)
c.add_page()
c.rect(200, 200, 90, 90)
c.save_pdf()
