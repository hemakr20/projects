import random
var = int(input("enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
du = "".join(random.sample(s, var))
print(du, end="")
