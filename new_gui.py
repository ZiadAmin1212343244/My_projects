from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
a = 75
c = 74
m = (2**16)+1

file_name = ""
seed = 0
##################### FUNCTIONS ########################
#Generate Numbers From file
def file_window():
    global file_name
    file_name = fd.askopenfilename()
    with open(file_name,"r") as file:
        seed = int(file.readline())
        for i in range(1000):
            seed = (a * seed + c) % m
            rich_text.insert(INSERT, str(i + 1) + "- ")
            rich_text.insert(INSERT, seed )
            rich_text.insert(INSERT, "\n")


# generate number from input
def num_input():
    global seed
    seed = int(file_path_entry.get())
    for i in range(1000):
        seed = (a * seed + c) % m
        rich_text.insert(INSERT, str(i+1) + "- ")
        rich_text.insert(INSERT, seed)
        rich_text.insert(INSERT, "\n")

# system Time function
def system_time():
    now = datetime.now()
    seed = now.hour + now.second + now.minute * now.microsecond
    rich_text.insert(INSERT, str(now) + "\n" )
    for i in range(1000):
        seed = (a * seed + c) % m
        rich_text.insert(INSERT, str(i + 1) + "- ")
        rich_text.insert(INSERT, seed)
        rich_text.insert(INSERT, "\n")


#button_generation
def button_function():
    rich_text.delete('1.0', END)
    Choice = v.get()
    if Choice == 1:    #1 file
        file_window()
        print(file_name)
        rich_text.insert(INSERT, "You chose to enter  a file\n")
        rich_text.insert(INSERT, file_name)

    elif Choice ==  2 : #2 input
        num_input()
    elif Choice == 3 : #3 system time
        system_time()





#################### GUI ###########################
#screen
screen = Tk()
screen.geometry("700x700")

#title
Title=Label(screen, text ="Pseudo number generator",font =("Arial" ,30))
Title.pack()  #to put the title in gui at top

#main frame
mainframe = Frame(screen)
mainframe.pack(pady = 60)







#label
#guess the number
guess_num_label = Label(mainframe,text = "Do you want to enter input or file name ? ", font=("Arial",20))
guess_num_label.pack(pady = 10)


#radio button
# value = {"Input" : 1,
#         "File" : 2,}

v = IntVar()

radio_button1 = Radiobutton(mainframe, text = "File", value = 1, variable = v, font = 18)
radio_button1.pack()

radio_button2 = Radiobutton(mainframe, text = "Input", value = 2 , variable = v,font = 18)
radio_button2.pack()


file_path_entry = Entry(mainframe, font = ("Arial",16))
file_path_entry.pack()

radio_button3 = Radiobutton(mainframe, text = "System Time", value = 3 , variable = v,font = 18)
radio_button3.pack()



# generate number button
file_path_button = Button(mainframe, text = 'Generate numbers', font = 25, command = button_function)
file_path_button.pack(pady = 15)

#rich text
rich_text  = ScrolledText(mainframe, width = 200, height = 200)
rich_text.pack(pady = 25)














screen.mainloop()

