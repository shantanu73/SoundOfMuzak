import os
import config
import random

l = [1,2,3,4,5]

y = random.shuffle(l)


# print(os.getcwd())
# print(type(os.getcwd()))
# path = os.getcwd()
#
#
# if os.getcwd() == "C:\\Users\\shantanu.dhiman\\PycharmProjects\\SoundOfMuzak":
#     print("\nYESSSS")
#
# for file in os.listdir("C:\\Users\\shantanu.dhiman\\PycharmProjects\\SoundOfMuzak"):
#     if file.endswith("-chain.pem"):
#         print(file)
#     if file.endswith("-key.pem"):
#         print(file)


print(config.Y)

config.Y = config.X + "b"

print(config.Y)

# if os.path.exists(path + *))
