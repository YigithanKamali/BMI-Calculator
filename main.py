from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a valid value !!!")
        return
    except SyntaxError:
        messagebox.showerror("ValueError","Please enter a valid value !!!")
        return
    if weight <= 0 or height <= 0:
        messagebox.showerror("Value Error" ,"Please enter a valid value !!!")
        return
    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        category = "Underweight"

    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"

    elif 25 <= bmi < 29.9:
        category = "Overweight"

    else:
        category = "Obese"


        # Display the result
    result_label.config(text=f'Your BMI: {bmi:.2f}\nCategory: {category}')

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)
window.config(padx=20,pady=20)

height_label = Label(text="Enter your height (cm)")
height_label.place(x=70, y=10)
height_entry = Entry(width=20)
height_entry.place(x=70, y=40)
height_entry.focus()

weight_label = Label(text="Enter your weight (kg)")
weight_label.place(x=70, y=70)
weight_entry = Entry(width=20)
weight_entry.place(x=70, y=100)

calculate_button = Button(window, text="Calculate", command=calculate_bmi)
calculate_button.pack()
calculate_button.place(x=90, y=130)


result_label = Label(window, text="")
result_label.pack()
result_label.place(x=70, y=160)

window.mainloop()