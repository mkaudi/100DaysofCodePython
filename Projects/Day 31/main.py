from tkinter import *
from random import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")
current_card = {}

def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=photo_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=photo_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")

def remove_word():
    to_learn.remove(current_card)
    change_word()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", mode="a")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="./images/card_front.png")
photo_back = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 260, image=photo_front)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=remove_word)
right_btn.grid(row=1, column=1)

change_word()

window.mainloop()
