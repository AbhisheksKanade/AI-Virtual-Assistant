from tkinter import*
from PIL import Image , ImageTk
from tkinter import LabelFrame
import action 
import Speech_to_text
root = Tk()
root.title("AI Assistant")
root.geometry("500x675")
root.resizable(False, FALSE)
root.config(bg = "#0b0b1a")

#ask fun
def ask():
    user_val = Speech_to_text.take_command()
    bot_val = action.action(user_val) 
    text.insert(END,'user --->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT <---" + str (bot_val) + "\n")
    if bot_val == "Shutting down the system":
        root.destroy()


    #Send fun
def Send():
    send = entry.get()
    bot_val = action.action(send)
    text.insert(END,'user --->' + send + "\n")
    if bot != None:
        text.insert(END, "BOT <---" + str (bot) + "\n")
    if bot == "Shutting down the system":
        root.destroy()
    


#ask fun
def Delete():
    text.delete(1.0, END)   



# frame

frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 3, relief = "raised")
frame.config(bg = "#0b0b1a")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

# textlable

text_lable = Label(frame, text = "AI Assistant", font = ("comic san ms", 14, "bold"), bg = "#222CB8")
text_lable.grid(row = 0, column = 0, padx = 20, pady = 10)

#image

image = ImageTk.PhotoImage(
  Image.open("/home/abhishekskanade/Desktop/python/AI virtual  assistance/image/robot.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

#Adding a text widget
text = Text(root, font = ('courier 10 bold'), bg = "#356696")
text.grid(row = 2, column = 0)
text.place(x = 70, y = 375, width = 375, height = 100)

#entry widget

entry = Entry(root, justify = CENTER)
entry.place(x=82, y=500, width=350, height=30)

#button1
Button1 = Button(root, text = "ASK", bg = "#356696", pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = ask)
Button1.place(x=30, y=575)

#button2
Button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=Send)
Button2.place(x=185, y=575)

#button3
Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=Delete)
Button3.place(x=340, y=575)







root.mainloop()  