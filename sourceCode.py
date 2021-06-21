from tkinter import *
import tkinter.font as tkFont
import webbrowser
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb  


class Window():
    def configure():
        global t
        t = Tk()
        t.title("Wikipedia Finder")
        t.iconbitmap(dir_path+r"\img\Wikipedia_Logo_1.0.ico")
        t.configure(bg=_from_rgb((28, 30, 38)))
        t.config(width=650,height=155)
    configure()    
    
    def fonts():
        global fontStyle
        fontStyle = tkFont.Font(family="Cascadia Mono", size=18)
        global fontButton
        fontButton = tkFont.Font(family="Cascadia Mono", size=15)
        global fontEnd
        fontEnd = tkFont.Font(family="Cascadia Mono", size=35)
    fonts()

    def a1_():
        global a1
        a1 = Label(t, text= "Input your country code:", fg=_from_rgb((212, 154, 121)), bg=_from_rgb((28, 30, 38)), font=fontStyle)
        a1.place(x=0,y=0)
    a1_()

    def b1_():
        global b1
        b1 = Entry(t, font=fontButton)
        b1.place(x=400, y=10)
        b1.configure({"background": _from_rgb((28, 30, 38))})
        b1.configure({"foreground": "peach puff"})
    b1_()

    def a2_():
        global a2
        a2= Label(t, text="Input what you want to see:", fg=_from_rgb((212, 154, 121)), bg=_from_rgb((28, 30, 38)), font=fontStyle)
        a2.place(x=0,y=50)
    a2_()

    def b2_():
        global b2
        b2 = Entry(t, font=fontButton)
        b2.place(x=400, y=55)
        b2.configure({"background": _from_rgb((28, 30, 38))})
        b2.configure({"foreground": _from_rgb((212, 154, 121))})
    b2_()

    class End():
        def naći():
            url = "https://"+b1.get()+".wikipedia.org/wiki/"+b2.get()
            webbrowser.open(url)
        g=Button(t, text="Find article", command=naći, bg=_from_rgb((28, 30, 38)), fg =_from_rgb((194, 70, 94)), font=fontButton, width=35)
        g.place(x=325,y=125, anchor="center")


t.mainloop()