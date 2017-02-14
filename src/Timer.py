import simplegui
import random

display = 'Hello World'
position = [50, 50]
width = 500
height = 500
interval = 2000
font_size = 24

def timer_handler():
    global position, font_size
    position[0] = random.randrange(0, width)
    position[1] = random.randrange(0, height)
    font_size += 1
    
# Input Handler
def input_handler(text):
    global display
    display = text

# Draw Handler
def draw(canvas):
    canvas.draw_text(display, position, font_size, "Green")

# Create Frame
frame = simplegui.create_frame('Change Position', 500, 500)

# Create Timer
timer = simplegui.create_timer(interval, timer_handler)

# Register Event Handlers
frame.add_input('Enter a Message : ', input_handler, 150)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
timer.start()