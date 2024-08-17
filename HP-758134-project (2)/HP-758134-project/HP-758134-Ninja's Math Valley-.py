# Name: Himil Patel 
# Description:
# This Python script uses Tkinter to create a math quiz game with multiple levels for an elementary school
# keeping in mind what they will be able to do. The Students will input answers through an entry widget,
# and the game provides them with a total number of correct and incorrect answers as you go through the
# game. Each level upgraded introduces new challenges, including random numbers and operators.
# Level 5, the most challenging level, includes a timer and division operation. The interface is easily
# accessible for users with buttons for different levels, reset, and quit. Instructions can be accessed
# through a button. 
# _________________________________________________________________________________________________________

import random
from tkinter import font
import tkinter.messagebox as messagebox
from tkinter import *
import time


def initialize_counters():
    global correct, incorrect, total, lbl_result_tru, lbl_result_fls
    incorrect = 0
    correct = 0
    total = 0
initialize_counters()

def ask_question_1():
    #Get new random numbers and operator
    global num1, num2, operator, current_level
   
    #Setting current level
    current_level = 1
   
    #Random operators and numbers
    num1 = random.randint(1, 3)
    num2 = random.randint(1, 3)
    operator = random.choice(["+", "-", "*"])

        
    #Update the labels with the new numbers and operator
    lbl_1["text"] = num1
    lbl_2["text"] = num2
    lbl_op["text"] = operator
    lvl_num.config(text="1")

    #Delete widget for the new question
    entry.delete(0, 'end')

def ask_question_2():
    #Get new random numbers and operator
    global num1, num2, operator, current_level
   
    #Setting current level
    current_level = 2
   
    #Random operators and numbers
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    operator = random.choice(["+", "-", "*"])

    #Update the labels with the new numbers and operator
    lbl_1["text"] = num1
    lbl_2["text"] = num2
    lbl_op["text"] = operator
    lvl_num.config(text="2")

    #Delete widget for the new question
    entry.delete(0, 'end')
   
def ask_question_3():
    #Get new random numbers and operator
    global num1, num2, operator, current_level
   
    #Setting current level
    current_level = 3
   
    #Random operators and numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operator = random.choice(["+", "-", "*"])

    #Update the labels with the new numbers and operator
    lbl_1["text"] = num1
    lbl_2["text"] = num2
    lbl_op["text"] = operator
    lvl_num.config(text="3")

    #Delete widget for the new question
    entry.delete(0, 'end')
       
def ask_question_4():
    #Get new random numbers and operator
    global num1, num2, operator, current_level, current_level
   
    #Setting current level
    current_level = 4
   
    #Random operators and numbers
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operator = random.choice(["+", "-", "*"])

    #Update the labels with the new numbers and operator
    lbl_1["text"] = num1
    lbl_2["text"] = num2
    lbl_op["text"] = operator
    lvl_num.config(text="4")

    #Delete widget for the new question
    entry.delete(0, 'end')
   
def ask_question_5():
    global num1, num2, operator, time_remaining, current_level, start_time

    #Setting current level
    current_level = 5

    #Random operators and numbers
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    operator = random.choice(["+", "-", "*", "%"])

    #Update the labels with the new numbers and operator
    lbl_1["text"] = num1
    lbl_2["text"] = num2
    lbl_op["text"] = operator
    lvl_num.config(text="5")

    #Delete widget for the new question
    entry.delete(0, 'end')

    #Start time
    start_time = time.time()

    #Variable to store the remaining time
    time_remaining = 10

    #Make the "Timer" label become visible
    lbl_timer.config(text=str("Timer:"))
    lbl_time.config(text=str(time_remaining))
    game_tab.after(1000, update_time)

def update_time():
    global time_remaining, current_level, correct, incorrect, total, start_time

    #Calculate time elapsed
    elapsed_time = time.time() - start_time
   
    #Calculate time remaining
    time_remaining = 10 - int(elapsed_time)

    if time_remaining > 0 and current_level == 5:
        lbl_time.config(text=str(time_remaining))
        game_tab.after(1000, update_time)
   
    elif current_level != 5:
        lbl_time.place_forget()
        lbl_timer.place_forget()
       
    else:        
        #Updating the "Incorrect" counter
        incorrect += 1
        counter_w.config(text=incorrect)
       
        #Updating the "Total attempts" counter
        total += 1
        counter_t.config(text=total)

        #Indicate the user that the answer is incorrect
        lbl_result_fls1.config(text="Incorrect!")
    
       
        #Chaning the place for the result labels
        lbl_result_fls1.place(relx = 0.5, rely = 0.5, anchor = 'center')
        
       
        #Making the "true" label dissapear
        lbl_result_tru1.place_forget()

       
        #Calling button 5
        ask_question_5()

def check_answer(event=None):
    global operator, correct, incorrect, total
    global time_remaining, lbl_result_tru, lbl_result_fls
    #Get the user's answer from the entry widget
    user_answer = entry.get()
   
    #Convert the user's answer to an integer
    try:  
        user_answer = int(user_answer)
    except ValueError:
        incorrect += 0
           
    #Calculate the correct answer using the random numbers and operator
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    elif operator == "*":
        correct_answer = num1 * num2
    elif operator == "%":
        correct_answer = num1 % num2
    else:
        correct_answer = 0
       
    #Update the "Current level" label
    lvl_num.config(text=current_level)

    #Updating the "Total attempts" counter
    total += 1
    counter_t.config(text=total)

    #Check if the user's answer is correct
    if user_answer == correct_answer:
        #Indicate the user that the answer is correct
        lbl_result_tru1.config(text="Correct!😀")
       
        #Changing the place for labels
        lbl_result_tru1.place(x=760, y=320)

       
        #Making the "false" label dissapear
        lbl_result_fls1.place_forget()
       
        #Updating the "Correct" counter
        correct += 1
        counter_c.config(text=correct)
    
       
    else:
        #Indicate the user that the answer is incorrect
        lbl_result_fls1.config(text="Incorrect!")

        lbl_result_fls1.place(x=760, y=320)

        #Making the "true" label dissapear
        lbl_result_tru1.place_forget()
       
        #Updating the "Incorrect" counter
        incorrect += 1
        counter_w.config(text=incorrect)
       
    #Calling new function from the appropriate level
    if current_level == 1:
        ask_question_1()
    elif current_level == 2:
        ask_question_2()
    elif current_level == 3:
        ask_question_3()
    elif current_level == 4:
        ask_question_4()
    elif current_level == 5:
        ask_question_5()

    #Delete the previous answer
    
    entry.delete(0, 'end')
       
def reset():
    global correct, incorrect, total
    #Updating the "Correct answers" counter
    correct = 0
    counter_c.config(text=correct)
   
    #Updating the "Incorrect answers" counter
    incorrect = 0
    counter_w.config(text=incorrect)
   
    #Updating the "Total answers" counter
    total = 0
    counter_t.config(text=total)
   
    #Updating the labels for "correct"
    lbl_result_tru1.config(text="")

   
    #Updating the lables for "Incorrect"
    lbl_result_fls1.config(text="")
    
def instr():
    message = "*********************************************************\n"
    message += "                                  Instructions         \n"
    message += "*********************************************************\n"
    message += "1. The game is divided into five levels, each level will be Progressively harder.\n\n"
    message += "2. In each level, a math problem will be displayed with random numbers and operators.\n\n"
    message += "3. You need to enter the correct answer in the submit section and press the 'Check' button.\n\n"
    message += "4. The game will indicate if your answer is correct or not.\n\n"
    message += "5. Press the 'Reset' button to reset the game.\n\n"
    message += "Levels:"
    message += "\nLevel 1 contains numbers from 1-3 and includes, +, -, *(multiplication)"
    message += "\n\nLevel 2 contains of numbers from 1-6 and includes, +, -, *"
    message += "\n\nLevel 3 contains of numbers from 1-9 and includes, +, -, *"
    message += "\n\nLevel 4 contains of numbers from 1-12 and includes, +, -, *"
    message += "\n\nLevel 5 inludes a timer and introduces a new operation, %(divison) it also contains numbers between 1-15. \n\n"
    message += "*********************************************************\n"
    message += "                             GOOD LUCK NINJAS!         \n"
    message += "*********************************************************\n"
    messagebox.showinfo("Instructions", message)
   
def notes():
    notes_button.pack_forget()
    results_txt.pack()
    back_button.pack()

def back():
    results_txt.pack_forget()
    back_button.pack_forget()
    notes_button.pack()
   
   
   
#Main screen
game_tab = Tk()
game_tab.title("Game")
game_tab.geometry("1024x768")


#Add the background image
background = PhotoImage(file = "game_wallpaper.png")
bg_label = Label(game_tab, image = background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#Widgets

#Label

#Button for level 1
lvl_1_btn = Button(game_tab, text= "Level 1", command=ask_question_1,\
                   font=("Arial",17), bg="#F0FCFE")
lvl_1_btn.place(x=10, y=450)

#Button for level 2
lvl_2_btn = Button(game_tab, text= "Level 2", command=ask_question_2,\
                   font=("Arial",17), bg="#B7D9E2")
lvl_2_btn.place(x=10, y=500)

#Button for level 3
lvl_3_btn = Button(game_tab, text= "Level 3", command=ask_question_3,\
                   font=("Arial",17), bg="#86B6C6")
lvl_3_btn.place(x=10, y=550)

#Button for level 4
lvl_4_btn = Button(game_tab, text= "Level 4",\
                   command=ask_question_4, font=("Arial",17), bg="#5C93AA")
lvl_4_btn.place(x=10, y=600)

#Button for level 5
lvl_5_btn = Button(game_tab, text= "Level 5",\
                   command=ask_question_5, font=("Arial",17), bg="#3A728E")
lvl_5_btn.place(x=10, y=650)

#Label for "="
lbl_equal = Label(game_tab, text="=", font=("Arial", 37))
lbl_equal.place(x=620, y=240)

#Submit button to check the users answer
submit_btn = Button(game_tab, text="Submit" \
                    , command=check_answer, font=("Last Ninja", 16), bg="#08c4b8")
submit_btn.place(x=760, y=250)

#Textbox for the user
entry = Entry(game_tab, width=5, font=("Arial", 24), bg="#fa5271")
entry.config(fg="#b8fa62")
entry.place(x=670,y=250)

#Allowing the user to click "enter" to check their answer
entry.bind('<Return>', check_answer)

#Button to reset
submit_btn = Button(game_tab, text="Reset", command=reset,\
                    font=("Arial", 17), bg="#fa5271")
submit_btn.place(x=10, y=700)

#Quit button for the user to stop playing
submit_btn = Button(game_tab, text="Quit", command=game_tab.destroy,\
                    font=("Last Ninja", 10), bg="#fa5271")
submit_btn.place(x=960, y=0)

#Label to keep track of the level
lvl = Label(game_tab, text="Current level:", font=("Arial", 17))
lvl.place(x=10, y=410)

lvl_num = Label(game_tab, text="0", font=("Arial", 16))
lvl_num.place(x=150, y=410)

#Create a button to show the instructions
btn_instr = Button(game_tab, text="Instructions", command=instr,\
                   font=("Last Ninja", 10), bg="#7393B3")
btn_instr.place(x=10, y=10)

#Changing the icon of my game
"""photo = PhotoImage(file = "Pokeball.png")
game_tab.iconphoto(False, photo)"""

#Counters
#Counter for correct answers
counter_c_1 = Label(game_tab, text="Correct answers:", font=("Arial", 16),\
                    fg="green")
counter_c_1.place(x=400, y=125)

#Counter for wrong answers
counter_w_1 = Label(game_tab, text=" Incorrect answers:", font=("Arial", 16),\
                    fg="red")
counter_w_1.place(x=615, y=125)

#Counter for total attempts
counter_t_1 = Label(game_tab, text="Total attempts:", font=("Arial", 16),\
                    fg="orange")
counter_t_1.place(x=200, y=125)

#Place holder
counter_c = Label(game_tab, text="0", font=("Arial", 16), fg="green",\
                  )
counter_c.place(x=567, y=125)

#Place holder
counter_w = Label(game_tab, text="0", font=("Arial", 16), fg="red",\
                  )
counter_w.place(x=801, y=125)

#Place holder
counter_t = Label(game_tab, text="0", font=("Arial", 16), fg="orange",\
                  )
counter_t.place(x=343, y=125)

#labels and images for results
#Correct
lbl_result_tru1 = Label(game_tab, text="", font=("Arial", 24), fg="green",\
                        bg="#b2fa72")
lbl_result_tru1.place(x=620, y=64)



#Incorrect
lbl_result_fls1 = Label(game_tab, text="", font=("Arial", 24), fg="red",\
                        bg="#b2fa72")
lbl_result_fls1.place(x=200, y=400)


#Printing the random numbers and operators
lbl_1 = Label(game_tab, text="?", font=("Times new Roman", 44))
lbl_1.place(x=150, y=240)

lbl_2 = Label(game_tab, text="?", font=("Times new Roman", 44))
lbl_2.place(x=480, y=240)

lbl_op = Label(game_tab, text="?", font=("Times new Roman", 44))
lbl_op.place(x=320, y=240)

#Extra widgets for level 5
#Label to display the time
lbl_time = Label(game_tab, text="", font=("Arial", 30))
lbl_time.place(x=420, y=350)

#Label for "timer"
lbl_timer = Label(game_tab, text="", font=("Arial", 30))
lbl_timer.place(x=300, y=350)

#Focusing on the text box
entry.focus()

#Run the main screen
game_tab.mainloop()