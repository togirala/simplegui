## Keyboard Echo

import simplegui

current_key = ' '
width = 35
height = 35
position = [10, 25]




def key_down(key):
    global current_key
    current_key = chr(key)
    
def key_up(key):
    global current_key
    current_key = ' '
    
def draw(canvas):
    canvas.draw_text(current_key, position, 20, 'Red')


# Frame
frame = simplegui.create_frame('Keyboard Echo', width, height)
frame.start()

# Keyboard Events
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

# Draw Event
frame.set_draw_handler(draw)