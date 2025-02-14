print("Welcome to BMI calculator!")
weight = input("What is your weight in kg? : ")
height = input("What is your height in cm? : ")
bmi = int(weight) / (int(height) / 100) ** 2
print("Your BMI is: ", int(bmi))