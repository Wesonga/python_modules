# body mass index (bmi)
# bmi = w/h**2

def calculate_bmi(weight, height):
    return weight / (height**2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is : {bmi}")
