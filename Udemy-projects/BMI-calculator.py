
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2 , 2)

if  BMI < 18.5:
   print(f"Your BMI is {BMI} and you are underweight")
elif BMI < 25:
   print(f"Your BMI is {BMI} and you have a normal weight")
elif BMI < 30:
   print(f"Your BMI is {BMI}and you are slightly overweight ")
elif BMI < 35:
   print(f"Your BMI is {BMI} and you are obese")
else:
  print(f"Your BMI is {BMI} and you are clinically obese")
