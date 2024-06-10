import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    

    # your code to animate Irma here
    data=open("data/irma.csv","r")
    lines=data.readlines()
    data.close()
    setposition=lines[1].strip().split(',')
    t.penup()
    t.goto((float(setposition[3])),(float(setposition[2])))
    t.pendown()
    
    
    
    
    for row in lines[1:]:
        values=row.strip().split(',')
        v1=float(values[2]) #Latitude
        v2=float(values[3])#Longitude
        if (float(values[4]))>+157:
            t.pensize(10)
            t.pencolor('Red')
            t.goto(v2,v1)
            t.write(str(5), align="center", font=("Arial", 12, "normal"))
        elif 157>(float(values[4]))>=130:
            t.pensize(8)
            t.pencolor('Orange')
            t.goto(v2,v1)
            t.write(str(4), align="center", font=("Arial", 12, "normal"))
        elif 130>(float(values[4]))>=111:
            t.pensize(6)
            t.pencolor('Yellow')
            t.goto(v2,v1)
            t.write(str(3), align="center", font=("Arial", 12, "normal"))
        elif 111>(float(values[4]))>=96:
            t.pensize(4)
            t.pencolor('Green')
            t.goto(v2,v1)
            t.write(str(2), align="center", font=("Arial", 12, "normal"))
        elif 96>(float(values[4]))>=74:
            t.pensize(2)
            t.pencolor('Blue')
            t.goto(v2,v1)
            t.write(str(1), align="center", font=("Arial", 12, "normal"))
        else:
            t.pensize(0)
            t.pencolor('White')
            t.goto(v2,v1)
            
            
    
    turtle.done()

if __name__ == "__main__":
    irma()
