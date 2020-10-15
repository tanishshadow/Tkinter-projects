from tkinter import *


class Calculator(Tk):
    """Making of a calculator using tkinter"""

    def screen(self):
        """Display for displaying calculation"""
        global screen_vr

        screen_vr = StringVar()
        screen_vr.set("")
        # Entry for the display
        self.sc = Entry(self, textvariable=screen_vr, font="timesnewroman 20 bold",
        borderwidth=5, relief=SUNKEN)
        self.sc.pack(
            side=TOP, ipadx="200", ipady="30", anchor="n", pady="5")

    def numKeys(self):
        """All the  buttons for the calculator"""
    # Frame for all rows
        # First row---
        self.frme1 = Frame(self)
        self.frme1.pack()
        self.numbers = ["1", "2", "3"]

        for number in self.numbers:
            b1 = Button(self.frme1, text=number, bg="gold", padx=50, pady=50)
            b1.pack(padx=0,
                    side=LEFT, anchor="w")
            b1.bind("<Button-1>",self.click)
        # second row

        self.numbers2 = ["4", "5", "6"]
        self.frme2 = Frame(self)
        self.frme2.pack()
        for number2 in self.numbers2:
            b2 = Button(self.frme2, text=number2, bg="gold", padx=50, pady=50)
            b2.pack(
                side=LEFT)
            b2.bind("<Button-1>",self.click)
        # 3rd row

        self.numbers3 = ["7", "8", "9"]
        self.frme3 = Frame(self)
        self.frme3.pack()
        for number3 in self.numbers3:
            b3 = Button(self.frme3, text=number3, bg="gold", padx=50, pady=50)
            b3.pack(
                side=LEFT)
            b3.bind("<Button-1>",self.click)



    def operators(self):
        """Keys such as + - = /"""

        b1 = Button(self.frme1, text="+", bg="silver", padx="50", pady="50")
        b1.pack(side=RIGHT)
        b1.bind("<Button-1>",self.click)
        b2 = Button(self.frme2, text="-", bg="silver", padx="50", pady="50")
        b2.pack(side=RIGHT)
        b2.bind("<Button-1>", self.click)
        b3 = Button(self.frme3, text="*", bg="silver", padx="50", pady="50")
        b3.pack(side=RIGHT)
        b3.bind("<Button-1>", self.click)
        fr4 = Frame(self)
        fr4.pack()
        b4 = Button(fr4, text="AC",
               padx="46", pady="47")
        b4.pack(side=LEFT)
        b4.bind("<Button-1>",self.click)
        b5 = Button(fr4, text="0",bg="gold",
               padx="50", pady="50")
        b5.pack(side=LEFT)
        b5.bind("<Button-1>", self.click)
        b6 = Button(fr4, text="=", bg="blue", padx='50', pady="50")
        b6.pack(side=LEFT)
        b6.bind("<Button-1>", self.click)
        b7 = Button(fr4, text="/", bg="silver",
               padx="50", pady="50")
        b7.pack(side=LEFT)
        b7.bind("<Button-1>", self.click)


    def click(self, event):
        try:

            txt = event.widget.cget("text")
            # print(txt)
            global screen_vr
            
            if txt == "=":
                try:
                    if screen_vr.get().isdigit():
                        value = int(screen_vr.get())
                    else:
                        value = eval(screen_vr.get())
                except Exception as e:
                    value = "Error"
                
                screen_vr.set(value)
                self.sc.update(screen_vr)
                self.sc.update(screen_vr)
            elif txt == "AC":
                screen_vr.set("")
                self.sc.update(screen_vr.get())
            else:
                screen_vr.set(screen_vr.get() + txt)
                self.sc.update(screen_vr)
                
        except Exception as n:
            pass

 
    
if __name__ == "__main__":
    root = Calculator()
    root.geometry("550x600")

    root.title("Calculator-Tanish Sarmah")
    root.screen()
    root.numKeys()
    root.operators()
    root.configure(bg="grey")
    root.mainloop()
