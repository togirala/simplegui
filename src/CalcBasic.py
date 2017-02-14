import simplegui

number1 = 0.0
number2 = 0.0
answer = 0.0

def show():
    global number1, number2
    print 'First Number is '+str(number1)
    print 'Second Number is '+str(number2)
    print "---------------------------"

def addition():
    global number1, number2, answer
    answer = number1 + number2
    print "#####", "Addition", "#####"
    output()
    #print number1, number2, output
    
def subraction():
    global number1, number2, answer
    answer = number1 - number2
    print "#####", "Subraction", "#####"
    output()
    #print number1, number2, output
    
def multiplication():
    global number1, number2, answer
    answer = number1*number2
    print "#####", "Multiplication", "#####"
    output()
    #print number1, number2, output
    
def division():
    global number1, number2, answer
    answer = number1 / number2
    print "#####", "Division", "#####"
    output()
    #print number1, number2, output

def output():
    global number1, number2, answer
    print 'First Number is '+str(number1)
    print 'Second Number is '+str(number2)
    print 'Output: '+str(answer)
    print "---------------------------"

def firstnumber(inp):
    global number1
    number1 = float(inp)
    print 'First Number is '+str(number1)
    print "---------------------------"
    #output()
    
def secondnumber(inp):
    global number2
    number2 = float(inp)
    print 'Second Number is '+str(number2)
    print "---------------------------"
    #output()

    

frame = simplegui.create_frame("Calculator", 200, 300)

frame.add_button("Show", show, 100)
frame.add_button("Add", addition, 100)
frame.add_button("Subract", subraction, 100)
frame.add_button("Multiply", multiplication, 100)
frame.add_button("Divide", division, 100)

frame.add_input("First Number", firstnumber, 150)
frame.add_input("Second Number", secondnumber, 150)


# Start the frame animation
frame.start()
