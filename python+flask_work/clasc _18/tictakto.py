import turtle as t

row_color = "green"
wind = t.Screen()
wind.bgcolor("black")
wind.tracer(0)

# tic_tak_to board

# row
row = t.Turtle()
row.shape("square")
row.color(row_color)
row.shapesize(stretch_wid=1, stretch_len=20)
row.penup()
row.goto(0, 0)
# row 2
row2 = t.Turtle()
row2.shape("square")
row2.color(row_color)
row2.shapesize(stretch_wid=1, stretch_len=20)
row2.penup()
row2.goto(0, 100)
# calm
row2 = t.Turtle()
row2.shape("square")
row2.color(row_color)
row2.shapesize(stretch_wid=20, stretch_len=1)
row2.penup()
row2.goto(80, 50)
# calm 2
row2 = t.Turtle()
row2.shape("square")
row2.color(row_color)
row2.shapesize(stretch_wid=20, stretch_len=1)
row2.penup()
row2.goto(-80, 50)
# player O
row2 = t.Turtle()
row2.shape("circle")
row2.color("red")
row2.shapesize(stretch_wid=3, stretch_len=3)
row2.penup()
row2.goto(0, 50)



while True:
    wind.update()

wind.mainloop()
