from tkinter import *
import time

tk = Tk()
tk.geometry("400x400")
windowWidth = 400
windowHeight = 400
paddleWidth = 100
paddleHeight = 20
canvas = Canvas(tk, width=windowWidth, height=windowHeight)

paddle = canvas.create_rectangle(0,0, paddleWidth, paddleHeight, fill="red")
canvas.move(paddle, windowWidth/2, windowHeight/2)
canvas.pack()

# X is a variable that drives our paddle.
# Along with updatePos, which will continually move the paddle
# by X (-10 or 10)
x=10
y=0

# Sets X to move the paddle in the negative direction (left)
def left(event):
    global x
    x = -10

# Sets X to move the paddle in the positive direction (right)
def right(event):
    global x
    x = 10

# Moves paddle by X continously
def moving(event):
    while True:
        tk.update()
        canvas.move(paddle, x, y)
        time.sleep(.1)

tk.bind("<KeyPress-Left>", left)
tk.bind("<KeyPress-Right>", right)
tk.bind("<KeyPress-Down>", moving)

tk.mainloop()
# How do we get to control the paddle with our functions?

# Main Loop, keeps the canvas updating
