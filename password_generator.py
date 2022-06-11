import random
passwordlen = int(input("Enter the length of the password"))
x="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
res = "".join(random.sample(x,passwordlen ))
print(res)
