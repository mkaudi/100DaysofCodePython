import tkinter

window =tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width=300, height=150)


def convert():
    output = round(float(to_convert.get())*1.6,3)
    answer.config(text=f"{output}")


equalsto_text = tkinter.Label(text="is equal to")
equalsto_text.grid(column=1, row=2)

to_convert = tkinter.Entry()
to_convert.grid(column=2, row=1)

answer = tkinter.Label(text="0")
answer.grid(column=2, row = 2)

miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=3, row=1)

km_text = tkinter.Label(text="Km")
km_text.grid(column=3, row=2)

calc_button = tkinter.Button(text="Calculate", command=convert)
calc_button.grid(column=2, row=3)


window.mainloop()