import  tkinter as tk
print("\n Hello Everyone Welcome!")
print("\n  BMI Calculator !")

window =tk.Tk()
window.title("BMI Calcualtor")
window.geometry("500x400")
title_label=tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 20)
)
title_label.pack()
weight_label=tk.Label(
    window,
    text="Weight(kg):"
)
height_label=tk.Label(
     window,
    text="Height(m):"
)
weight_label.pack()
weight_entry=tk.Entry(window)
weight_entry.pack()
height_label.pack()
height_entry=tk.Entry(window)
height_entry.pack()

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            result_label.config(
                text="Height and weight must be greater than zero."
            )
            return

        bmi = bmi_calc(height, weight)

        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal"

        elif bmi < 30:
            category = "Overweight"

        elif bmi < 35:
            category = "Obese"

        else:
            category = "Clinically obese"

        result_label.config(
            text=f"Your BMI is {bmi}\nCategory: {category}"
        )

    except ValueError:
        result_label.config(
            text="Please enter valid numbers."
        )

calculate_buttton=tk.Button(
      window,
      text="Calculate BMI" ,
      command=calculate_bmi
)
calculate_buttton.pack()
result_label=tk.Label(
      window,
      text="" ,
      font=("Arial", 14)
 )
result_label.pack()
window.mainloop()