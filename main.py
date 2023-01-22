from cgitb import text
from textwrap import fill
import tkinter
from tkinter import *
from tkinter.tix import COLUMN
from tkinter.ttk import Style
from turtle import color
import customtkinter
import pandas
import random
from tkinter import messagebox
import time

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Data Read

dataset = pandas.read_csv('///your path here///')
data_dic = dataset.to_dict(orient='records')
#print(data_dic)


# UI setup
root = customtkinter.CTk()
root.title('Vocabularator')
root.geometry(f"{900}x{600}")
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=1)
root.grid_rowconfigure((0, 1, 2, 3), weight=1)


# Functions & Variables

target_lan = tkinter.IntVar(value=1)

global curr_word
curr_word = random.choice(data_dic)

def chg2dk():
    lght_md.deselect()
    
    word_canvas.config(bg='#2B2B2B')
    word_canvas.itemconfig(canvas_text,fill='white')
    customtkinter.set_appearance_mode('Dark')
def cgh2lght():
    drk_md.deselect()
    
    word_canvas.config(bg='#DBDBDB')
    word_canvas.itemconfig(canvas_text,fill='black')
    customtkinter.set_appearance_mode('Light')
    
def help_popup():
    messagebox.showinfo('Help', "Hunty, you're helpless :(")

def next_word():
    global curr_word
    curr_word = random.choice(data_dic)
    word_canvas.itemconfig(canvas_text, text=curr_word['English'])

    

def check_word():
    global curr_word
    curr_input = usr_inp.get()
    print(curr_input)
    print(curr_word['Swedish'].lower())
    usr_inp.delete(0,END)

    if curr_input.lower() == curr_word['Swedish'].lower():
        print('correct')
        curr_word = 'Correct!'
        word_canvas.itemconfig(canvas_text, text=curr_word)   
        word_canvas.after(1500, next_word)      
    else:
        print('incorrect')
        curr_word = 'The right answer was: '+ curr_word['Swedish']
        word_canvas.itemconfig(canvas_text, text=curr_word)   
        word_canvas.after(3500, next_word)





 
# Elements

side_frame = customtkinter.CTkFrame(root, width=250, corner_radius=0)
side_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
side_frame.grid_rowconfigure(4, weight=1)

word_canvas = Canvas(root, width=400, height=300,bg='#2B2B2B', highlightthickness=0)
word_canvas.grid(row=1, column=1, columnspan=2, pady=(50,0),padx=(45,0))


btn_quit = customtkinter.CTkButton(master=root, text='Quit', hover=True, command=root.quit)
btn_quit.grid(row=4, column=3, pady=(0,15))

btn_help = customtkinter.CTkButton(master=side_frame, text='Help', hover=True, command=help_popup)
btn_help.grid(row=1, column=0, pady=(30,00), padx=30)

btn_next = customtkinter.CTkButton(master=root, text='Skip', hover=True, command=next_word)
btn_next.grid(row=3, column=1, padx=(120,5), pady=(5,25))

btn_check = customtkinter.CTkButton(master=root, text='Check', hover=True, command=check_word)
btn_check.grid(row=3, column=2, padx=(5,90),pady=(5,25))


rad_frame = customtkinter.CTkFrame(master=root, width=200,height=200, corner_radius=10)
rad_frame.grid(row=1, column=3,padx=30, pady=50)
rad_eng = customtkinter.CTkRadioButton(master=rad_frame, text='From English', variable=target_lan, value=1)
rad_eng.grid(row=1, column=3, pady=10, padx=(20,5))
rad_swe = customtkinter.CTkRadioButton(master=rad_frame, text='From Swedish', variable=target_lan, value=2, state='disabled')
rad_swe.grid(row=2, column=3, pady=10, padx=(20,5))

usr_inp = customtkinter.CTkEntry(master=root, width=370, border_width=1, corner_radius=10, placeholder_text='Your answer here...',text_color='silver')
usr_inp.grid(row=2,column=1,columnspan=2, pady=(50,0), padx=(40,0))

drk_md = customtkinter.CTkSwitch(master=side_frame,text='Dark Mode', command=chg2dk)
drk_md.grid(row=2, column=0, pady=(455,0))
lght_md = customtkinter.CTkSwitch(master=side_frame, text='Light Mode', command=cgh2lght)
lght_md.grid(row=3, column=0, padx=10)


canvas_text = word_canvas.create_text(200, 150, font=('center', 25), fill='white', width=350)





# Default Values

drk_md.select()
rad_eng.select()

# Functions

next_word()


# Main Loop

root.mainloop()
