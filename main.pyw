from tkinter import *

root = Tk()
width = 4
height = 4

#def print(text, grid_position=None):
    # text = str(text)
    # lbl = Label(root, text=text)
    # if grid_position is None:
    #     lbl.pack()
    # else:
    #     lbl.grid(grid_position)


def input(text=None, grid_position=None):
    if text is not None:
        text = str(text)
        lbl = Label(root, text=text)
        if grid_position is None:
            lbl.pack()
        else:
            lbl.grid(grid_position)
    textbox = Entry(root)
    textbox.pack()
    value = False
    # check if user has clicked button
    while value is False:
        def button():
            value = True

        btn = Button(root, text="Next", command=button, padx=50, pady=50, fg='red', bg='green')
        btn.pack()
    text = textbox.get()

    return text


def store(number):
    entry.insert(END, number)


def operators(operator):
    entry.insert(END,operator)
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, columnspan=3, column=0, padx=10, pady=10)


def equal():
    entry.get(0,END)


# put buttons on screen
def buttons():
    btn_0 = Button(root, bg='#808080',padx=40, pady=20, text='0', fg='black', command=lambda: store(0), height=height,
                   width=width).grid(row=5, column=0)
    btn_1 = Button(root, bg='#808080', padx=40, pady=20, text='1', fg='black', command=lambda: store(1), height=height,
                   width=width).grid(row=4, column=0)
    btn_2 = Button(root, bg='#808080', padx=40, pady=20, text='2', fg='black', command=lambda: store(2), height=height,
                   width=width).grid(row=4, column=1)
    btn_3 = Button(root, bg='#808080', padx=40, pady=20, text='3', fg='black', command=lambda: store(3), height=height,
                   width=width).grid(row=4, column=2)
    btn_4 = Button(root, bg='#808080', padx=40, pady=20, text='4', fg='black', command=lambda: store(4), height=height,
                   width=width).grid(row=3, column=0)
    btn_5 = Button(root, bg='#808080', padx=40, pady=20, text='5', fg='black', command=lambda: store(5), height=height,
                   width=width).grid(row=3, column=1)
    btn_6 = Button(root, bg='#808080', padx=40, pady=20, text='6', fg='black', command=lambda: store(6), height=height,
                   width=width).grid(row=3, column=2)
    btn_7 = Button(root, bg='#808080', padx=40, pady=20, text='7', fg='black', command=lambda: store(7), height=height,
                   width=width).grid(row=3 - 1, column=0)
    btn_8 = Button(root, bg='#808080', padx=40, pady=20, text='8', fg='black', command=lambda: store(8), height=height,
                   width=width).grid(row=3 - 1, column=1)
    btn_9 = Button(root, bg='#808080', padx=40, pady=20, text='9', fg='black', command=lambda: store(9), height=height,
                   width=width).grid(row=3 - 1, column=2)


def symbols():
    btn_plus = Button(root,padx=40, pady=20, text='+',bg='white',  fg='black', command=lambda:operators('+'), height=height, width=width).grid(column=3, row=1)
    btn_minus = Button(root,padx=40, pady=20, text='-', bg='white', fg='black', command=lambda:operators('-'), height=height, width=width).grid(column=3, row=2)
    btn_times = Button(root,padx=40, pady=20, text='×', bg='white', fg='black', command=lambda:operators('×'), height=height, width=width).grid(column=3, row=3)
    btn_divide = Button(root,padx=40, pady=20, text='÷',bg='white',  fg='black', command=lambda:operators('÷'), height=height, width=width).grid(column=3, row=4)


# equal sign

btn_equal = Button(root,padx=40, pady=20, text='=',bg='white',  command=equal,fg='black', height=height, width=width).grid(row=5, column=3)
buttons()
symbols()
root.mainloop()
