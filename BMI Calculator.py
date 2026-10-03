print("\n Hello Everyone Welcom!")
print("\n  BMI CALCULATOR !")
while True:
    print("Type 'q'to quit")
    height_input=input("Enter your height in m: ")
    if height_input.lower()=="q":
        print("Goodbye")
        break
    
    weight_input=input("Enter your weight in kg: ")
    if height_input.lower()=="q":
        print("Goodbye")
        break
    try:
        height=float(height_input)
        weight=float(weight_input)
    except ValueError:
        print("Plese enetr valid number")
        if height <=0 or weight<=0:
            print("Heigh and weight must be graterthan zero.")
            continue
def bmi_calcu(height, weight):
    return round(weight/height**2,2)
def bmi_calcu(bmi):
    if bmi < 18.5:
        print(f"your BMI is {bmi}, is under weight")
            
    elif bmi < 25:
            print(f"your BMI is {bmi}, is normal")
    elif bmi < 30:
                print(f"your BMI is {bmi}, is overweight")
    elif bmi < 35:
                print(f"your BMI is {bmi}, is obese")
    else:
          print("You are clinically obese")
print(bmi_calcu)
