import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

def draw_rectangle(width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_circle(radius, color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

# Draw toilet base
t.penup()
t.goto(-50, -100)
t.setheading(0)
t.pendown()
draw_rectangle(100, 100, 'lightgrey')

# Draw toilet tank
t.penup()
t.goto(-60, 0)
t.setheading(0)
t.pendown()
draw_rectangle(120, 60, 'grey')

# Draw toilet seat
t.penup()
t.goto(-40, 0)
t.setheading(0)
t.pendown()
draw_rectangle(80, 10, 'black')

# Draw head popping out of the toilet lid
t.penup()
t.goto(0, 10)  # Positioned just above the toilet lid
t.setheading(0)
t.pendown()
t.color("peachpuff")
draw_circle(30, "peachpuff")

# Draw cute eyes (big, with shine)
for eye_x in [-10, 10]:
    t.penup()
    t.goto(eye_x, 40)  # Position eyes on the head
    t.pendown()

    # Draw the white part of the eye
    t.color("white")
    draw_circle(10, "white")

    # Draw the black pupil
    t.penup()
    t.goto(eye_x, 42)  # Move slightly higher for better pupil placement
    t.pendown()
    t.color("black")
    draw_circle(5, "black")

    # Draw the shine in the eye for cuteness
    t.penup()
    t.goto(eye_x - 3, 46)  # Shine to the top left of the eye
    t.pendown()
    t.color("white")
    draw_circle(2, "white")  # Small white circle for shine

# Draw mouth (under eyes)
t.penup()
t.goto(-10, 25)
t.setheading(-60)
t.pendown()
t.color("black")
t.circle(10, 120)

# Write a label
t.penup()
t.goto(-50, -150)
t.pendown
t.write("SKIBIDI TOILET", font=("Arial", 16, "bold"))

# Write a label
t.penup()
t.goto(-50, -150)
t.pendown
t.write("SKIBIDI TOILET", font=("Arial", 16, "bold"))

# Separate block for click counter functionality
click_count = 0  # Initialize the counter

# Create a separate turtle for the click counter text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Display "Click Me!" text initially
text_turtle.goto(-50, 100)  # Position the text above the drawing
text_turtle.write("Click Me!", font=("Arial", 16, "bold"))

def on_click(x, y):
    global click_count
    # Check if the click is within the Skibidi Toilet drawing area
    if -50 <= x <= 50 and -100 <= y <= 60:  # Adjust these bounds as needed
        click_count += 1
        text_turtle.clear()  # Clear the previous text (including "Click Me!")
        text_turtle.goto(-50, 100)  # Position the text above the drawing
        text_turtle.write(f"Skibidi Toilet clicked! Count: {click_count}", font=("Arial", 16, "bold"))

# Bind the click event to the on_click function
screen = turtle.Screen()
screen.onclick(on_click)

# Hide turtle and finish
t.hideturtle()
turtle.done()