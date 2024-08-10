from tkinter import *
import time
window = Tk()
window.title('Clock by igagamer(faiz)')
window.geometry('600x400')
def myTime():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    myText = hour + ':' + minute + ':' + second
    myLabel.config(text=myText)
    myLabel.after(1000, myTime)
myLabel = Label (window, text="",font=('arial', 72), fg='yellow',bg='red' )
myLabel.pack()
myTime()
window.mainloop()
