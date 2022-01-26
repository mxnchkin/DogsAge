import tkinter

window = tkinter.Tk()
window.geometry("312x324")

window.title("Number Calculator")

label = tkinter.Label(window, text="Calculate").grid()

enter_number = tkinter.Label(window, font="Arial", text="enter a number").grid(row=1, column=0)
tkinter.Entry(window).grid(row=1, column=1)



button_widget = tkinter.Button(window,text="Calculate").grid(row=3, column=1)
button_widget.grid()









window.mainloop()
