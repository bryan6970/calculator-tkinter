import webbrowser

from cgitb import reset
from tkinter import *

import tkinter
import math
from PIL import ImageTk, Image
import tkinter.font as font
from webbrowser import Chrome

root = Tk()
root.title('Calculator')

root.iconphoto(False, ImageTk.PhotoImage(file='C:\\Users\\wong2\\Documents\\coding\\coding pics\\calculator.webp'))
myFont = font.Font(size=15)
pady = 7
padx = 35
width = 4
height = 4
try:

    # def print(text, grid_position=None):
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
        global word
        try:
            if word is True:
                entry.configure(state='normal')
                entry.delete(0, END)
                entry.configure(state='disabled')
                word = False
        except:
            pass
        if number == 'delete':
            entry.configure(state='normal')
            entry.delete(0, END)
            entry.configure(state='disabled')
        else:
            entry.configure(state='normal')
            entry.insert(END, number)
            entry.configure(state='disabled')


    def operators(operator):
        entry.configure(state='normal')
        entry.insert(END, operator)
        entry.configure(state='disabled')
        global word
        word = False


    # textbox
    entry = Entry(root, width=35, borderwidth=5, font=myFont, fg='black', disabledforeground='black')

    entry.grid(row=0, columnspan=5, column=0, padx=10, pady=10)


    def delete1():
        entry.configure(state='normal')
        entry.delete(len(entry.get()) - 1, END)
        entry.configure(state='disabled')


    def equal():
        equation = (entry.get())
        almost_ready_equation = equation.replace("÷", '/')
        ready_equation = almost_ready_equation.replace('×', '*')
        entry.configure(state='normal')
        entry.delete(0, END)
        entry.configure(state='disabled')
        try:
            result = eval(ready_equation)
            entry.configure(state='normal')
            entry.insert(0, result)
            entry.configure(state='disabled')
        except:
            entry.configure(state='normal')
            entry.delete(0, END)
            entry.configure(state='disabled')
        global word
        word = True


    # put buttons on screen
    def buttons():
        
        button_dict = {}
        button_list = ['C', '.', '00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(button_list)):
            button_dict[button_list[i]] = Button(root, bg='#808080', padx=padx, pady=pady, text=button_list[i], fg='black', 
                    disabledforeground='black',
                       command=lambda x=button_list[i]: store(x),
                       height=height,
                       width=width, font=myFont).grid(row=5 - (i // 3), column=i % 3)


    def symbols():
        btn_plus = Button(root, padx=padx, pady=pady, text='+', bg='white', fg='black', disabledforeground='black',
                          command=lambda: operators('+'),
                          height=height, width=width, font=myFont).grid(column=3, row=1)
        btn_minus = Button(root, padx=padx, pady=pady, text='-', bg='white', fg='black', disabledforeground='black',
                           command=lambda: operators('-'),
                           height=height, width=width, font=myFont).grid(column=3, row=2)
        btn_times = Button(root, padx=padx, pady=pady, text='×', bg='white', fg='black', disabledforeground='black',
                           command=lambda: operators('×'),
                           height=height, width=width, font=myFont).grid(column=3, row=3)
        btn_divide = Button(root, padx=padx, pady=pady, text='÷', bg='white', fg='black', disabledforeground='black',
                            command=lambda: operators('÷'),
                            height=height, width=width, font=myFont).grid(column=3, row=4)
        btn_plus.grid(column=3, row=1)
        btn_minus.grid(column=3, row=2)
        btn_times.grid(column=3, row=3)
        btn_divide.grid(column=3, row=4)


    def open_browser():
        # chrome.open_new('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih9avnrrn5AhVYIbcAHYw8DQkQwqsBegQIAhAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU')
        # webbrowser.get('chrome').open('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih9avnrrn5AhVYIbcAHYw8DQkQwqsBegQIAhAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU')

        url = 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih9avnrrn5AhVYIbcAHYw8DQkQwqsBegQIAhAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.open(url)

        webbrowser.register('chrome', None,
                            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
        webbrowser.open(url)


    def ad():
        btn_ad = Button(root, pady=pady + 41.49, text='#GETBETTER', fg='darkblue', width=16, command=open_browser).grid(
            column=2, row=1)


    # equal sign

    btn_equal = Button(root, padx=padx + 8, pady=pady + 19, text='=', bg='white',
                       command=equal, fg='black', height=height, width=width).grid(row=5, column=3)

    # delete button
    btn_delete = Button(root, height=4, width=10,pady=7, padx=2, text='DEL', fg='black', disabledforeground='black', bg='#808080',
                        command=delete1,
                        font=myFont).grid(column=1, row=1)
    ad()
    buttons()
    symbols()

except:
    entry.configure(state='normal')
    entry.delete(0, END)
    entry.configure(state='disabled')
root.mainloop()
