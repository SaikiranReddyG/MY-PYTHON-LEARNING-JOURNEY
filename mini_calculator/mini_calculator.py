from tkinter import *
"""imports  all the fuctions and modules from tkinter"""


def click(event):
    global ScValue   # making it a global variable to allow the function to acess and modify
    text = event.widget.cget("text")
    # widget refers to button that triggered th event
    # cget(text)--retives the text associated with the clicked button and assign it variable text
    print(text)
    if text == "=":  # if we press equal to sign
        if ScValue.get().isdigit():   # if the button pressed is a digit
            value = int(ScValue.get())  # assign the digit value to the "value" variable
        else:   # if the button pressed is not a digit
            try:
                value = eval(screen.get())   # evaluate the button pressed for exception
            except Exception as e:  # consider the exception as e variable
                print(e)
                value = "Error"  # show error on the screen

        ScValue.set(value)   # set the scvalue to value
        screen.update()  # update the screen with new value

    elif text == "C":   # if the button pressed is c
        ScValue.set("")   # set screen value to empty
        screen.update()  # update the screen

    else:
        ScValue.set(ScValue.get() + text)    # give the screen value the entered text
        screen.update()    # update the screen


root = Tk()   # creating tkinker window
root.geometry("465x580")  # sets the initial size of the window
root.minsize(465, 575)  # sets the max and min size of the window
root.maxsize(465, 584)
root.title("calculator digital")
root.wm_iconbitmap("calculator.ico")  # setting the icon of the window
root.configure(bg="yellow")

ScValue = StringVar()  # store the value displayed on the screen
ScValue.set("")   # set it to empty in the begining
screen = Entry(root, textvariable=ScValue, font="lucida 30 bold")
"""
creates an entry widget
the entry widget is a text input field to display the input and output
textVariable is given as scValue, so any change in that will automatically update the screen display
"""
screen.pack(fill=X, ipadx=20, pady=15, padx=10)
"""
pack meathod is used to place the entry widget within the root window
fill x--ensures the widget expands horizontally to fill available space
"""

# Frame 1 which include 9, 8, 7 & C

frame = Frame(root, bg="green")  # creates a frame widget to the root window with bg clr
b1 = Button(frame, text="9", font="lucid 35 bold", )  # create the button
b1.pack(side=LEFT, padx=10, pady=5)  # pack the button to left side of the frame
b1.bind("<Button-1>", click)  # when the button is clicked the click function is called

b2 = Button(frame, text="8", font="lucid 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame, text="7", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

b4 = Button(frame, text="C", font="lucida 35 bold", padx=38)
b4.pack(side=RIGHT, padx=10, pady=5)
b4.bind("<Button-1>", click)
frame.pack(fill=X)

# Frame 2 which include 6, 5, 4 & %

frame2 = Frame(root, bg="green")
b1 = Button(frame2, text="6", font="lucida 35 bold")
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame2, text="5", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame2, text="4", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

b4 = Button(frame2, text="%", font="lucida 35 bold", padx=34)
b4.pack(side=RIGHT, padx=10, pady=5)
b4.bind("<Button-1>", click)
frame2.pack(fill=X)

# Frame 3 which include 3, 2, 1 & (+ -)

frame3 = Frame(root, bg="green")
b1 = Button(frame3, text="3", font="lucida 35 bold")
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame3, text="2", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame3, text="1", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

frame0 = Frame(frame3, bg="gray")
b4 = Button(frame0, text="+", font="lucida 35 bold", padx=5)
b4.pack(side=RIGHT, pady=5)
b4.bind("<Button-1>", click)

b5 = Button(frame0, text="-", font="lucida 35 bold", padx=7)
b5.pack(side=RIGHT, pady=5)
b5.bind("<Button-1>", click)
frame0.pack(side=RIGHT, padx=10, fill=X)
frame3.pack(fill=X)

# Frame 4 which include ., 0, = & * /

frame4 = Frame(root, bg="green")
b1 = Button(frame4, text=".", font="lucida 35 bold", padx=7.1)
b1.pack(side=LEFT, padx=10, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(frame4, text="0", font="lucida 35 bold")
b2.pack(side=LEFT, padx=10, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(frame4, text="=", font="lucida 35 bold")
b3.pack(side=LEFT, padx=10, pady=5)
b3.bind("<Button-1>", click)

frame0 = Frame(frame4, bg="green")
b4 = Button(frame0, text="*", font="lucida 35 bold", padx=8)
b4.pack(side=RIGHT, pady=5)
b4.bind("<Button-1>", click)

b5 = Button(frame0, text="/", font="lucida 35 bold", padx=10)
b5.pack(side=RIGHT, pady=5)
b5.bind("<Button-1>", click)
frame0.pack(side=RIGHT, padx=10, fill=X)
frame4.pack(fill=X)

frame5 = Frame(root, bg="green")
b = Button(text="Close", command=quit, font="bold 30", bg="red", fg="yellow")
b.pack(fill=X)
frame5.pack(fil=X)

root.mainloop()
