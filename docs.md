# Table of Contents

* [p5skia.canvas](#p5skia.canvas)
  * [Canvas](#p5skia.canvas.Canvas)
    * [\_\_init\_\_](#p5skia.canvas.Canvas.__init__)
    * [resize](#p5skia.canvas.Canvas.resize)
    * [background](#p5skia.canvas.Canvas.background)
    * [clear](#p5skia.canvas.Canvas.clear)
    * [fill](#p5skia.canvas.Canvas.fill)
    * [alpha](#p5skia.canvas.Canvas.alpha)
    * [stroke](#p5skia.canvas.Canvas.stroke)
    * [stroke\_weight](#p5skia.canvas.Canvas.stroke_weight)
    * [no\_fill](#p5skia.canvas.Canvas.no_fill)
    * [no\_stroke](#p5skia.canvas.Canvas.no_stroke)
    * [antialias](#p5skia.canvas.Canvas.antialias)
    * [text\_font](#p5skia.canvas.Canvas.text_font)
    * [text\_size](#p5skia.canvas.Canvas.text_size)
    * [text\_style](#p5skia.canvas.Canvas.text_style)
    * [line](#p5skia.canvas.Canvas.line)
    * [ellipse](#p5skia.canvas.Canvas.ellipse)
    * [circle](#p5skia.canvas.Canvas.circle)
    * [quad](#p5skia.canvas.Canvas.quad)
    * [rect](#p5skia.canvas.Canvas.rect)
    * [triangle](#p5skia.canvas.Canvas.triangle)
    * [arc](#p5skia.canvas.Canvas.arc)
    * [text](#p5skia.canvas.Canvas.text)
    * [text\_box](#p5skia.canvas.Canvas.text_box)
    * [load\_font](#p5skia.canvas.Canvas.load_font)
    * [load\_image](#p5skia.canvas.Canvas.load_image)
    * [image](#p5skia.canvas.Canvas.image)
    * [load\_video](#p5skia.canvas.Canvas.load_video)
    * [draw](#p5skia.canvas.Canvas.draw)
    * [add\_page](#p5skia.canvas.Canvas.add_page)
    * [push](#p5skia.canvas.Canvas.push)
    * [pop](#p5skia.canvas.Canvas.pop)
    * [translate](#p5skia.canvas.Canvas.translate)
    * [rotate](#p5skia.canvas.Canvas.rotate)
    * [scale](#p5skia.canvas.Canvas.scale)
    * [save](#p5skia.canvas.Canvas.save)
    * [save\_frame](#p5skia.canvas.Canvas.save_frame)
    * [save\_pdf](#p5skia.canvas.Canvas.save_pdf)
    * [start\_video](#p5skia.canvas.Canvas.start_video)
    * [save\_video\_frame](#p5skia.canvas.Canvas.save_video_frame)
    * [finish\_video](#p5skia.canvas.Canvas.finish_video)

<a id="p5skia.canvas"></a>

# p5skia.canvas

<a id="p5skia.canvas.Canvas"></a>

## Canvas Objects

```python
class Canvas()
```

<a id="p5skia.canvas.Canvas.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int = DEFAULT_WIDTH,
             height: int = DEFAULT_HEIGHT,
             show: bool = False,
             renderer: Literal["GPU", "CPU", "PDF"] = "GPU",
             fps: float = 60.0,
             title: str = DEFAULT_TITLE,
             output: Optional[str] = None)
```

Create a canvas

**Arguments**:

- `width` _int_ - width of canvas
- `height` _int_ - height of canvas
- `show` _bool_ - show the canvas
- `renderer` _str_ - renderer to use (GPU, CPU, PDF)
- `fps` _float_ - desired frames per second
- `title` _str_ - title of window
- `output` _str_ - output path for PDF renderer

<a id="p5skia.canvas.Canvas.resize"></a>

#### resize

```python
def resize(width: int, height: int) -> None
```

Resizes the canvas

**Arguments**:

- `width` _int_ - width
- `height` _int_ - height

<a id="p5skia.canvas.Canvas.background"></a>

#### background

```python
def background(r: float, g: float, b: float, a=1.0)
```

Set the background color

**Arguments**:

- `r` _float_ - red value
- `g` _float_ - green value
- `b` _float_ - blue value
- `a` _float_ - alpha value (default: 1.0)

<a id="p5skia.canvas.Canvas.clear"></a>

#### clear

```python
def clear()
```

Clear the canvas

<a id="p5skia.canvas.Canvas.fill"></a>

#### fill

```python
def fill(r: float, g: float, b: float, a: float = 1.0)
```

Set the fill color

**Arguments**:

- `r` _float_ - red value
- `g` _float_ - green value
- `b` _float_ - blue value
- `a` _float_ - alpha value (default: 1.0)

<a id="p5skia.canvas.Canvas.alpha"></a>

#### alpha

```python
def alpha(a: float)
```

Set the alpha value of images drawn to the canvas

**Arguments**:

- `a` _float_ - alpha value

<a id="p5skia.canvas.Canvas.stroke"></a>

#### stroke

```python
def stroke(r: float, g: float, b: float, a: float = 1.0)
```

Set the stroke color

**Arguments**:

- `r` _float_ - red value
- `g` _float_ - green value
- `b` _float_ - blue value
- `a` _float_ - alpha value (default: 1.0)

<a id="p5skia.canvas.Canvas.stroke_weight"></a>

#### stroke\_weight

```python
def stroke_weight(w: float)
```

Set the stroke weight

**Arguments**:

- `w` _float_ - stroke weight

<a id="p5skia.canvas.Canvas.no_fill"></a>

#### no\_fill

```python
def no_fill()
```

Disable fill

<a id="p5skia.canvas.Canvas.no_stroke"></a>

#### no\_stroke

```python
def no_stroke()
```

Disable stroke

<a id="p5skia.canvas.Canvas.antialias"></a>

#### antialias

```python
def antialias(antialias: bool)
```

Set antialias

**Arguments**:

- `antialias` _bool_ - antialias

<a id="p5skia.canvas.Canvas.text_font"></a>

#### text\_font

```python
def text_font(fontname: str)
```

Set the text font

**Arguments**:

- `fontname` _str_ - font name

<a id="p5skia.canvas.Canvas.text_size"></a>

#### text\_size

```python
def text_size(size: float)
```

Set the text size

**Arguments**:

- `size` _float_ - font size

<a id="p5skia.canvas.Canvas.text_style"></a>

#### text\_style

```python
def text_style(s: Literal["bold", "bolditalic", "italic", "normal"])
```

Set the text style

**Arguments**:

- `s` _str_ - text style (bold, bolditalic, italic, normal)

<a id="p5skia.canvas.Canvas.line"></a>

#### line

```python
def line(x1: float, y1: float, x2: float, y2: float)
```

Draw a line

**Arguments**:

- `x1` _float_ - x1
- `y1` _float_ - y1
- `x2` _float_ - x2
- `y2` _float_ - y2

<a id="p5skia.canvas.Canvas.ellipse"></a>

#### ellipse

```python
def ellipse(x: float, y: float, w: float, h: float)
```

Draw an ellipse

**Arguments**:

- `x` _float_ - x
- `y` _float_ - y
- `w` _float_ - width
- `h` _float_ - height

<a id="p5skia.canvas.Canvas.circle"></a>

#### circle

```python
def circle(x: float, y: float, d: float)
```

Draw a circle

**Arguments**:

- `x` _float_ - x
- `y` _float_ - y
- `d` _float_ - diameter

<a id="p5skia.canvas.Canvas.quad"></a>

#### quad

```python
def quad(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float,
         x4: float, y4: float)
```

Draw a quad

**Arguments**:

- `x1` _float_ - x1
- `y1` _float_ - y1
- `x2` _float_ - x2
- `y2` _float_ - y2
- `x3` _float_ - x3
- `y3` _float_ - y3
- `x4` _float_ - x4
- `y4` _float_ - y4

<a id="p5skia.canvas.Canvas.rect"></a>

#### rect

```python
def rect(x: float,
         y: float,
         w: float,
         h: float,
         tl: Optional[float] = None,
         tr: Optional[float] = None,
         br: Optional[float] = None,
         bl: Optional[float] = None)
```

Draw a rectangle

**Arguments**:

- `x` _float_ - x
- `y` _float_ - y
- `w` _float_ - width
- `h` _float_ - height
- `tl` _float_ - top left corner radius
- `tr` _float_ - top right corner radius
- `br` _float_ - bottom right corner radius
- `bl` _float_ - bottom left corner radius

<a id="p5skia.canvas.Canvas.triangle"></a>

#### triangle

```python
def triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float)
```

Draw a triangle

**Arguments**:

- `x1` _float_ - x1
- `y1` _float_ - y1
- `x2` _float_ - x2
- `y2` _float_ - y2
- `x3` _float_ - x3
- `y3` _float_ - y3

<a id="p5skia.canvas.Canvas.arc"></a>

#### arc

```python
def arc(x, y, w, h, start, stop)
```

Draw an arc. An arc is a section of an ellipse defined by the x, y, w, and h parameters. x and y set the location of the arc's center. w and h set the arc's width and height. Start and stop, set the angles between which to draw the arc. Arcs are always drawn clockwise from start to stop.

**Arguments**:

- `x` _float_ - x
- `y` _float_ - y
- `w` _float_ - w
- `h` _float_ - h
- `start` _float_ - start angle
- `stop` _float_ - stop angle

<a id="p5skia.canvas.Canvas.text"></a>

#### text

```python
def text(text: str, x: float, y: float)
```

Draw text

**Arguments**:

- `text` _str_ - text to draw
- `x` _float_ - x
- `y` _float_ - y

<a id="p5skia.canvas.Canvas.text_box"></a>

#### text\_box

```python
def text_box(text: str,
             x: float,
             y: float,
             w: float | None,
             h: float | None = None,
             line_height: float | None = None,
             align: Literal["left", "right", "center", "justify"] = "left",
             valign: Literal["top", "center", "bottom"] = "top")
```

Draw text in a box.

**Arguments**:

- `text` _str_ - text to draw
- `x` _float_ - x
- `y` _float_ - y
- `w` _float|None_ - width
- `h` _float|None_ - height
- `line_height` _float|None_ - line height
- `align` _str_ - horizontal text alignement ("left", "right", "center", "justify")
- `valign` _str_ - vertical text alignement ("top", "center", "bottom")

<a id="p5skia.canvas.Canvas.load_font"></a>

#### load\_font

```python
def load_font(path: str) -> skia.Typeface
```

Load a font

**Arguments**:

- `path` _str_ - path to font file

<a id="p5skia.canvas.Canvas.load_image"></a>

#### load\_image

```python
def load_image(path: str) -> skia.Image
```

Load an image

**Arguments**:

- `path` _str_ - path to image file

<a id="p5skia.canvas.Canvas.image"></a>

#### image

```python
def image(image: skia.Image,
          x: float,
          y: float,
          w: Optional[float] = None,
          h: Optional[float] = None)
```

Draw an image

If w and h are None, the image will be drawn at its original size. If only w or only h is None, the image will be drawn based on the given dimension, maintaining its aspect ratio.

**Arguments**:

- `image` _skia.Image_ - image to draw
- `x` _float_ - x
- `y` _float_ - y
- `w` _Optional[float]_ - width
- `h` _Optional[float]_ - height

<a id="p5skia.canvas.Canvas.load_video"></a>

#### load\_video

```python
def load_video(path: str) -> Video
```

Load a video

**Arguments**:

- `path` _str_ - path to video file

**Returns**:

- `Video` - Video object

<a id="p5skia.canvas.Canvas.draw"></a>

#### draw

```python
def draw()
```

Draw the canvas

<a id="p5skia.canvas.Canvas.add_page"></a>

#### add\_page

```python
def add_page(width: Optional[float] = None, height: Optional[float] = None)
```

Add a page to a PDF canvas

**Arguments**:

- `width` _float_ - width of page
- `height` _float_ - height of page

<a id="p5skia.canvas.Canvas.push"></a>

#### push

```python
def push()
```

Push the canvas state

<a id="p5skia.canvas.Canvas.pop"></a>

#### pop

```python
def pop()
```

Pop the canvas state

<a id="p5skia.canvas.Canvas.translate"></a>

#### translate

```python
def translate(x: float, y: float)
```

Translate the canvas

**Arguments**:

- `x` _float_ - x
- `y` _float_ - y

<a id="p5skia.canvas.Canvas.rotate"></a>

#### rotate

```python
def rotate(deg: float)
```

Rotate the canvas

**Arguments**:

- `deg` _float_ - degrees to rotate

<a id="p5skia.canvas.Canvas.scale"></a>

#### scale

```python
def scale(sx: float, sy: Optional[float] = None)
```

Scale the canvas

**Arguments**:

- `sx` _float_ - x scale
- `sy` _float_ - y scale

<a id="p5skia.canvas.Canvas.save"></a>

#### save

```python
def save(filename: str = "frame.png")
```

Save the canvas to a file

**Arguments**:

- `filename` _str_ - filename to save to

<a id="p5skia.canvas.Canvas.save_frame"></a>

#### save\_frame

```python
def save_frame(filename: Optional[str] = None)
```

Save a frame. If filename is None, it will be named frame_0000000000.jpg

**Arguments**:

- `filename` _str_ - filename to save to

<a id="p5skia.canvas.Canvas.save_pdf"></a>

#### save\_pdf

```python
def save_pdf()
```

Save the PDF canvas

<a id="p5skia.canvas.Canvas.start_video"></a>

#### start\_video

```python
def start_video(filename: str = "sketch.mp4",
                fps: int = 60,
                frames: int = 0,
                input_params: Optional[list[str]] = None,
                output_params: Optional[list[str]] = None)
```

Save a video

**Arguments**:

- `filename` _str_ - filename to save to
- `fps` _float_ - frames per second
- `frames` _int_ - maximum number of frames to record
- `input_params` _Optional[list]_ - Additional ffmpeg input command line parameters.
- `output_params` _Optional[list]_ - Additional ffmpeg output command line parameters.

<a id="p5skia.canvas.Canvas.save_video_frame"></a>

#### save\_video\_frame

```python
def save_video_frame()
```

Save a video frame

<a id="p5skia.canvas.Canvas.finish_video"></a>

#### finish\_video

```python
def finish_video()
```

Finish recording a video

