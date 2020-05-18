import random, string

length_of_password = int(input("What length of password do you want?"))

password = ""
c = string.ascii_letters + string.digits + string.punctuation
for x in range(length_of_password):
    password += "".join(random.choices(c))

print (password)
