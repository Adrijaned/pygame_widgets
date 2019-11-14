from pygame_widgets.constants.public import THECOLORS, SRCALPHA, button_bg, frame
from pygame_widgets.auxiliary import cursors


class DEFAULT:
    cursor = cursors.arrow

    class WINDOW:
        fps = 25
        color = THECOLORS['gray90']

    class TEXT:
        bg = THECOLORS['transparent']
        font_color = THECOLORS['black']
        font = 'calibri'
        font_size = 16
        text = ""
        bold = False
        italic = False
        underlined = False
        smooth = True

        class Alignment:
            x = 1
            y = 1

    class IMAGE:
        bg = THECOLORS['white']

    class BUTTON:
        bg_normal = button_bg(THECOLORS['gray80'], THECOLORS['gray65'])
        bg_mouseover = button_bg(THECOLORS['lightblue1'], THECOLORS['blue'])
        bg_pressed = button_bg(THECOLORS['lightblue3'], THECOLORS['blue'])
        cursor_mouseover = cursor_pressed = cursors.arrow

    class ENTRY:
        bg = frame(THECOLORS['white'], THECOLORS['blue'])
        cursor = cursors.textmarker

        class Alignment:
            x = 0
            y = 1

        class Boundary_space:
            top = 3
            left = 6
            bottom = 3
            right = 6

        class Text:
            font_color = THECOLORS['black']
            highlight_font_color = THECOLORS['white']
            highlight_bg = THECOLORS['blue']
            font = 'calibri'
            font_size = 16
            bold = False
            italic = False
            underlined = False
            smooth = True
            text = "Hello World"

        class Cursor:
            color = THECOLORS['black']


SUPER = 's'  # kwarg used to detect if the class is initialising as super() or not
PYGAME_EVENTS = range(1, 18)
