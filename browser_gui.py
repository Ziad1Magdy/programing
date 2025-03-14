from tkinter import *
import webbrowser

def get_link():
    link = my_text.get()
    webbrowser.open(link)

my_frame = Tk()
my_frame.title("browse App")
my_frame.geometry("500x300")

my_lable = Label(my_frame, text="Web Browser", font="Tahoma 30 bold")
my_lable.pack(pady=20)

my_text = Entry(my_frame, width=50)
my_text.pack(pady=20)

my_button = Button(my_frame, text="Click Here To Go !", fg= "black", bg="#d6b588",font= "Helvatica 10 bold", command=get_link)
my_button.pack()

my_frame.mainloop()
