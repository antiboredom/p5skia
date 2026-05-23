from p5skia import Canvas

c = Canvas(width=600, height=600, show=True)

paragraph = "A spectre is haunting Europe – the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies.\n\nWhere is the party in opposition that has not been decried as communistic by its opponents in power? Where is the opposition that has not hurled back the branding reproach of communism, against the more advanced opposition parties, as well as against its reactionary adversaries?"

while c.draw():
    c.background(0.9, 0.9, 0.9)

    c.text_font("Times New Roman")
    c.text_size(15)

    c.no_stroke()
    c.fill(0, 0, 0)

    c.text_box(paragraph, 10, 0, 100, 100)

    c.text_font("Arial")
    c.text_size(12)
    c.text_box(paragraph, 20, 100, 300, align="justify")

    c.text_font("Impact")
    c.text_size(14)
    c.text_box(paragraph, 220, 250, 300, 300, line_height=20, align="center")
