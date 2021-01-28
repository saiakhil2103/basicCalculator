# import necessary modules
from tkinter import *

# create window
window = Tk()

def display(x):
    if screen.get() == '0':
        screen.set(x)
        return
    result = str(screen.get())
    result = result + str(x)
    screen.set(result)

def equals():
    try:
        result = screen.get()
        if 'x' in result:
            result = result.replace('x','*')
            #print(result)
        result = eval(str(result))
        screen.set(result)
    except:
        pass
    


# set window title
window.title('Calculator')

# set window geometry
window.geometry('200x300')

f1 = Frame(window, relief = SUNKEN, bd = 5)
f1.pack(fill = X)

f2 = Frame(window, padx = 5, bg = '#bacbcf')
f2.pack(fill = X)

screen = StringVar()
screen.set('0')
entry = Entry(f1, textvariable = screen, font = ('Helvetica', '25'), bg = '#e1e7e8')
entry.pack(fill = X)

b7 = Button(f2, text = '7', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('7'))
b7.grid(row = 0, column = 0, padx = 3, pady = 3)
b8 = Button(f2, text = '8', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('8'))
b8.grid(row = 0, column = 1, padx = 3, pady = 3)
b9 = Button(f2, text = '9', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('9'))
b9.grid(row = 0, column = 2, padx = 3, pady = 3)
bAdd = Button(f2, text = '+', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('+'))
bAdd.grid(row = 0, column = 3, padx = 3, pady = 3)

b4 = Button(f2, text = '4', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('4'))
b4.grid(row = 1, column = 0, padx = 3, pady = 3)
b5 = Button(f2, text = '5', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('5'))
b5.grid(row = 1, column = 1, padx = 3, pady = 3)
b6 = Button(f2, text = '6', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('6'))
b6.grid(row = 1, column = 2, padx = 3, pady = 3)
bSub = Button(f2, text = '-', font = ('Helvetica', '20'), padx = 5, bg = '#bcdfe6', command = lambda : display('-'))
bSub.grid(row = 1, column = 3, padx = 3, pady = 3)

b1 = Button(f2, text = '1',font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('1'))
b1.grid(row = 2, column = 0, padx = 3, pady = 3)
b2 = Button(f2, text = '2', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('2'))
b2.grid(row = 2, column = 1, padx = 3, pady = 3)
b3 = Button(f2, text = '3', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('3'))
b3.grid(row = 2, column = 2, padx = 3, pady = 3)
bMul = Button(f2, text = 'x', font = ('Helvetica', '20'), padx = 3, bg = '#bcdfe6', command = lambda : display('x'))
bMul.grid(row = 2, column = 3, padx = 3, pady = 3)

b0 = Button(f2, text = '0', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('0'))
b0.grid(row = 3, column = 0, padx = 3, pady = 3)
bDot = Button(f2, text = '.', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = lambda : display('.'))
bDot.grid(row = 3, column = 1, padx = 3, pady = 3)
bE = Button(f2, text = '=', font = ('Helvetica', '20'), padx = 2, bg = '#bcdfe6', command = equals)
bE.grid(row = 3, column = 2, padx = 3, pady = 3)
bDiv = Button(f2, text = '/', font = ('Helvetica', '20'), padx = 4, bg = '#bcdfe6', command = lambda : display('/'))
bDiv.grid(row = 3, column = 3, padx = 3, pady = 3)

window.mainloop()

