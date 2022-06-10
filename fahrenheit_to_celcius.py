def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
n= int(input("Enter the temperature in fahrenheit"))
print(convert(n))
