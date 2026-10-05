print("\n Hello Everyone Welcome!")
print("\n  BMI Calculator!")
def bmi_calcu(height, weight):
    return round(weight/height**2,2)
while True:
    print("Type 'q'to quit")
    height_input=input("Enter your height in m: ").strip()
    if height_input.lower()=="q":
        print("Goodbye")
        break
    
    weight_input=input("Enter your weight in kg: ").strip()
    if height_input.lower()=="q":
        print("Goodbye")
        break
    try:
        height=float(height_input)
        weight=float(weight_input)
    except ValueError:
        print("Plese enetr valid number")
        continue
    if height <=0 or weight<=0:
        print("Please enter Valid number .")
        continue
    bmi = bmi_calcu(height,weight)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are under weight")
            
    elif bmi < 25:
            print(f"Your B0.5MI is {bmi},  you are normal")
    elif bmi < 30:
                print(f"Your BMI is {bmi}, you are overweight")
    elif bmi < 35:
                print(f"Your BMI is {bmi}, you are obese")
    else:
          print("You are Clinically obese")

