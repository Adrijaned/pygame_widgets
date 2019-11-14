print("pygame_widgets init")

import pygame
pygame.init()
from pygame_widgets.widgets.widget import *
from pygame_widgets.widgets.holder import *
from pygame_widgets.widgets.text import *
from pygame_widgets.widgets.button import *
from pygame_widgets.widgets.image import *
from pygame_widgets.widgets.entry import *
# from pygame_widgets.constants import *
import pygame_widgets.constants as constants
from pygame_widgets.auxiliary.event_mode import set_mode_init, set_mode_mainloop, get_mode


def new_loop():
    pygame.event.post(pygame.event.Event(constants.PYGAME_WIDGETS, ID=constants.E_LOOP_STARTED))
    try:
        del delayed_call.queue[0]
        for func, args, kwargs in delayed_call.queue[0]:
            func(*args, **kwargs)
    except IndexError:
        pass


def delayed_call(func, delay=1, *args, **kwargs):
    if len(delayed_call.queue) <= delay:
        delayed_call.queue += [list() for _ in range(delay - len(delayed_call.queue) + 1)]
    delayed_call.queue[delay].append((func, args, kwargs))
delayed_call.queue = list()


print("pygame_widgets initialised")
