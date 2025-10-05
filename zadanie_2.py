import turtle

def tree_Pifagor(t, order, size):
    if order == 0:
        t.forward(size)
        t.backward(size)
    else:
        t.forward(size)          
        t.left(30)               
        tree_Pifagor(t, order-1, size*0.7)  
        t.right(60)              
        tree_Pifagor(t, order-1, size*0.7)  
        t.left(30)               
        t.backward(size)         


def main():
    screen = turtle.Screen()
    screen.title("дерево Піфагора")
    

    t = turtle.Turtle()
    t.speed(0)

    
    while True:
        try:
            order = int(input("Рівень рекурсії: "))
            if order < 0:
                print("Рівень рекурсії повинен бути >= 0")
                continue
            break
        except ValueError:
            print("Рівень рекурсії повинен бути цілим число ")

    
    t.penup()
    t.goto(0, -250)
    t.setheading(90)  
    t.pendown()

    tree_Pifagor(t, order=order, size=100)  

    screen.mainloop()

if __name__ == "__main__":
    main()
