from turtle import*
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for index, mau in enumerate(colors):
    color(mau,mau)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()