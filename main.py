from guizero import *

def meme():
    drawing.clear()
    drawing.bg = "yellow"
    drawing.image(0, 0, "meomeo.jpg", width=photo_slider.value, height=photo_slider.value)
    drawing.text(
        align.value, vertical.value, toptext.value, color=color.value, size=slider.value, font=font.value
    )
    drawing.text(
        align.value, vertical.value + spacing.value, bottomtext.value, color=color.value, size=slider.value, font=font.value
    )

app = App("guizero", width=800, height=800)

# Configuration options column
config_box = Box(app, layout="grid", grid=[0, 0], align="left")

Text(config_box, "Top Text", grid=[0, 0], align="left")
toptext = TextBox(config_box, command=meme, grid=[1, 0])

Text(config_box, "Bottom Text", grid=[0, 1], align="left")
bottomtext = TextBox(config_box, command=meme, grid=[1, 1])

Text(config_box, "Text Color", grid=[0, 2], align="left")
color = Combo(config_box, options=["red", "green", "blue", "white", "black"], command=meme, grid=[1, 2])

Text(config_box, "Font", grid=[0, 3], align="left")
font = Combo(config_box, options=["Times New Roman", "Arial", "Courier New"], command=meme, grid=[1, 3])

Text(config_box, "Image Size", grid=[0, 4], align="left")
photo_slider = Slider(config_box, start=500, end=1000, horizontal=True, command=meme, grid=[1, 4])

Text(config_box, "Text Size", grid=[0, 5], align="left")
slider = Slider(config_box, start=10, end=1000, horizontal=True, command=meme, grid=[1, 5])

Text(config_box, "Horizontal Align", grid=[0, 6], align="left")
align = Slider(config_box, start=0, end=500, horizontal=True, command=meme, grid=[1, 6])

Text(config_box, "Vertical Align", grid=[0, 7], align="left")
vertical = Slider(config_box, start=0, end=500, horizontal=False, command=meme, grid=[1, 7])

Text(config_box, "Spacing", grid=[0, 8], align="left")
spacing = Slider(config_box, start=0, end=500, horizontal=False, command=meme, grid=[1, 8])

# Drawing area column
drawing = Drawing(app, width="500", height="500",  align="right")

meme()

app.display()
