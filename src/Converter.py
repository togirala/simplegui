import simplegui

display = 'Welcome!'

def convert(value):
    dollars = int(value)
    cents = round(100*(value-dollars))
    
    dollar_string = convert_units(dollars, 'dollar')
    cents_string  = convert_units(cents, 'cent')
    
    if dollars != 0 and cents != 0:
        return dollar_string + ' and ' + cents_string
        
    elif dollars == 0:
        return cents_string
        
    elif cents == 0:
        return dollar_string
        
    elif dollars == 0 & cents == 0:
        return 'You Have no Money'
        
    else:
        # This should never happen
        return "You are screwed!"

    
def convert_units(value, name):
    if value > 1:
        name = name+'s'
        string = str(int(value)) + ' ' + name
        
    else:
        string = str(int(value)) + ' ' + name
        
    return string

# Input Handler
def input_handler(text):
    global display
    display = float(text)


# Draw Handler
def draw(canvas):
    if display == 'Welcome!':
        canvas.draw_text(display, [100, 150], 24, "Green")
    else:
        canvas.draw_text(convert(display), [100, 150], 24, "White")
    

# Create Frame
frame = simplegui.create_frame('Converter', 500, 300)

# Register Event Handlers
frame.add_input('Enter a value : ', input_handler, 150)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()