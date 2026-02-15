# valentine_day

import turtle

Mrs_Bro = 'Bro, will you be my Valentine!'

def draw_rose():
     
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("hotpink")

     
    for i in range(160):
        t.circle(190 - i, 90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(180)
        if i > 120:
            t.color("green")
    
    t.hideturtle()
    print("Yay! Here is a rose for you 😘 😍 ")
    turtle.done()

 
while True:
    print(Mrs_Bro)
    ask = input('Yes or No: ').lower().strip()
    
    if ask == 'yes':
         
        draw_rose()
        break
    else:
        # print("\nWrong answer... try again.\n")
        print('Are u sure 🤔')