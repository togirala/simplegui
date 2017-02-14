import simplegui
#import random

second_duration = 1000
minute_duration = 60000
hour_duration = 3600000
seconds_past = 0
minutes_past = 0
hours_past = 0
font_size = 56
position = [35, 125]
    
    
def seconds():
#    print 'seconds'
    global seconds_past, minutes_past, hours_past
    seconds_past += 1
    if seconds_past == 60:
        seconds_past = 0
    return seconds_past

def minutes():
#    print 'minutes'
    global seconds_past, minutes_past, hours_past
    minutes_past += 1
    if minutes_past == 60:
        minutes_past = 0
    return minutes_past

def hours():
#    print 'hours'
    global seconds_past, minutes_past, hours_past
    hours_past += 1
    if hours_past == 24:
        hours_past = 0
    return hours_past


#print str(hours_past) + ':' + str(minutes_past) + ':' + str(seconds_past)

def time():
    display = str(hours_past) + ':' + str(minutes_past) + ':' + str(seconds_past)
    return display
    
    
# Draw Handler
def draw(canvas):
    canvas.draw_text(time(), position, font_size, "Green")

# Create Frame
frame = simplegui.create_frame('Change Position', 200, 200)

def start_timer():
    if second_timer.is_running() == False:
        second_timer.start()
        minute_timer.start()
        hour_timer.start()

def stop_timer():
    if second_timer.is_running() == True:
        second_timer.stop()
        minute_timer.stop()
        hour_timer.stop()   
        
def reset_timer():
    global seconds_past, minutes_past, hours_past
    seconds_past = 0
    minutes_past = 0
    hours_past = 0 
    return seconds_past, minutes_past, hours_past

# Register Event Handlers

frame.add_button('Start', start_timer, 100)
frame.add_button('Stop', stop_timer, 100)
frame.add_button('Reset', reset_timer, 100)



# Draw Handler
frame.set_draw_handler(draw)


# Create Timer
second_timer = simplegui.create_timer(second_duration, seconds)
minute_timer = simplegui.create_timer(minute_duration, minutes)
hour_timer = simplegui.create_timer(hour_duration, hours)


# Start the frame animation
frame.start()
#second_timer.start()
#minute_timer.start()
#hour_timer.start()


