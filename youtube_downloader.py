import os
from tkinter import *

win = Tk()
win.geometry("360x280")

def run():
	os.startfile("link.bat")

def download():
	with open("link.bat","w") as dwnld:
		dwnld.write(f'youtube-dl {link.get()}')
		dwnld.close()
	run()

f = Frame(win)
f.grid()
Label(f,text="Youtube Video Downloader").pack()

f1 = Frame(win)
f1.grid()
Label(f1,text="Enter link").grid(row=1)

link = StringVar()

Entry(f1,textvariable=link).grid(row=1,column=1)

btn = Button(f1,text="Download",relief=RAISED,command=download)
btn.grid(column=1,pady=5)

win.mainloop()