from tkinter import *
root = Tk()
root.geometry('500x300')

topFrame = Frame(root)
topFrame.pack()



button1 = Button(topFrame,text='Button1',fg = 'red')
button2 = Button(topFrame,text='Button2',fg = 'blue')
button3 = Button(topFrame,text='Button3',fg = 'green')


button1.pack()
button2.pack()
button3.pack()


root.mainloop()
