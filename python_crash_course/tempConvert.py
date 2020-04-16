prompt = "Enter temperature (ex: 30C or 30F): "
temp = input(prompt)
temp = temp.title()
print("You entered: " + temp)

def convertCelciusToFarenheit(temp_in_c):
    return (temp_in_c * 9/5.0 ) + 32.0

def convertFarenheitToCelcius(temp_in_f):
    return (temp_in_f - 32) * (5.0/9.0)
if temp[-1] == 'C':
    print(temp + " in Farenheit is: " + format(convertCelciusToFarenheit(int(temp[0:-1]))) + " F")
elif temp [-1] == 'F':
    print(temp + " in Celcius is: " + format(convertFarenheitToCelcius(int(temp[0:-1]))) + " C")
else:
    print("Bad input")