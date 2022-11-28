# التمرين الاول
firstName = 'Abdulrahman'
lastName = 'alshamari'
age = 34
hobby = 'developing games'

print(" First Name : ", firstName, "\n Last Name : ", lastName, "\n i am ", age, " ,my hobby is ", hobby)

# التمرين الثاني

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your Weight in Kg: "))

BMI = weight / (height * height)
print("BMI Calculated is:  ", BMI)

if (BMI > 0):
    if (BMI <= 16):
        print("You are very underweight")
    elif (BMI <= 18.5):
        print("You are underweight")
    elif (BMI <= 25):
        print("Congrats! You are Healthy")
    elif (BMI <= 30):
        print("You are overweight")
    else:
        print("You are very overweight")
else:
    print("enter valid details")

#Bonus
# Define function to convert Fahrenheit to celsius

def ConvertFtoC(tempF):
    # Convert the Fahrenheit into Celsius

    tempC = (5 / 9) * (tempF - 32)

    # Return the conversion value

    return tempC


# Take the Fahrenheit value from the user

tempF = float(input("Enter the temperature in Fahrenheit: "))

# Print the Fahrenheit value

print("Temperature in Fahrenheit = {:.2f}".format(tempF))

# Print the Celsius value

print("Temperature in Celsius = {:.2f}".format(ConvertFtoC(tempF)))
